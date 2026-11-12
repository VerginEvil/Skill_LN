use regex::Regex;

/// Encapsulates selection attributes for `<Selection>` in ControlArea.
#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct BdeSelection {
    pub attributes: Vec<String>,
}

impl BdeSelection {
    pub fn new() -> Self {
        Self { attributes: Vec::new() }
    }

    pub fn from_fields(fields: &[&str]) -> Self {
        Self {
            attributes: fields.iter().map(|s| s.to_string()).collect(),
        }
    }

    pub fn add_selection(&mut self, attribute: &str) {
        if !self.attributes.iter().any(|a| a == attribute) {
            self.attributes.push(attribute.to_string());
        }
    }

    pub fn add(&mut self, attribute: &str) {
        self.add_selection(attribute);
    }

    pub fn to_xml(&self) -> String {
        if self.attributes.is_empty() {
            return String::new();
        }
        let mut xml = String::from("<Selection>");
        for attr in &self.attributes {
            xml.push_str("<selectionAttribute>");
            xml.push_str(&escape_xml(attr));
            xml.push_str("</selectionAttribute>");
        }
        xml.push_str("</Selection>");
        xml
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum ComparisonOperator {
    Eq,
    Ne,
    Lt,
    Le,
    Gt,
    Ge,
    Like,
}

impl ComparisonOperator {
    pub fn as_str(&self) -> &'static str {
        match self {
            Self::Eq => "eq",
            Self::Ne => "ne",
            Self::Lt => "lt",
            Self::Le => "le",
            Self::Gt => "gt",
            Self::Ge => "ge",
            Self::Like => "like",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum LogicalOperator {
    And,
    Or,
}

impl LogicalOperator {
    pub fn as_str(&self) -> &'static str {
        match self {
            Self::And => "and",
            Self::Or => "or",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum FilterExpression {
    Comparison {
        operator: ComparisonOperator,
        attribute: String,
        value: String,
    },
    Logical {
        operator: LogicalOperator,
        expressions: Vec<FilterExpression>,
    },
}

impl FilterExpression {
    pub fn to_xml(&self) -> String {
        match self {
            Self::Comparison { operator, attribute, value } => {
                let mut xml = String::from("<ComparisonExpression>");
                xml.push_str("<comparisonOperator>");
                xml.push_str(operator.as_str());
                xml.push_str("</comparisonOperator>");
                xml.push_str("<attributeName>");
                xml.push_str(&escape_xml(attribute));
                xml.push_str("</attributeName>");
                if value.is_empty() {
                    xml.push_str("<emptyValue/>");
                } else {
                    xml.push_str("<instanceValue>");
                    xml.push_str(&escape_xml(value));
                    xml.push_str("</instanceValue>");
                }
                xml.push_str("</ComparisonExpression>");
                xml
            }
            Self::Logical { operator, expressions } => {
                let mut xml = String::from("<LogicalExpression>");
                xml.push_str("<logicalOperator>");
                xml.push_str(operator.as_str());
                xml.push_str("</logicalOperator>");
                for expr in expressions {
                    xml.push_str(&expr.to_xml());
                }
                xml.push_str("</LogicalExpression>");
                xml
            }
        }
    }
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct BdeFilter {
    pub expression: Option<FilterExpression>,
}

impl BdeFilter {
    pub fn new() -> Self {
        Self { expression: None }
    }

    pub fn with_expression(expr: FilterExpression) -> Self {
        Self { expression: Some(expr) }
    }

    pub fn from_raw(expr_str: &str) -> Self {
        Self::parse(expr_str).unwrap_or_else(|| {
            Self {
                expression: parse_single_condition(expr_str),
            }
        })
    }

    /// Parses string filter expression (e.g. `field == 'val'`, `x >= 10`, `a == 'b' AND c LIKE 'd*'`).
    pub fn parse(expr_str: &str) -> Option<Self> {
        let trimmed = expr_str.trim();
        if trimmed.is_empty() {
            return None;
        }

        let expr = parse_filter_str(trimmed)?;
        Some(Self { expression: Some(expr) })
    }

    pub fn to_xml(&self) -> String {
        match &self.expression {
            Some(expr) => format!("<Filter>{}</Filter>", expr.to_xml()),
            None => String::new(),
        }
    }
}

fn parse_single_condition(condition: &str) -> Option<FilterExpression> {
    let re = Regex::new(r"(?i)^([a-zA-Z0-9_.$]+)\s*(==|!=|<=|>=|<>|=|<|>|LIKE)\s*(.*)$").ok()?;
    let caps = re.captures(condition.trim())?;

    let field = caps.get(1)?.as_str().trim().to_string();
    let op_str = caps.get(2)?.as_str().trim().to_uppercase();
    let raw_val = caps.get(3)?.as_str().trim();

    let val = if (raw_val.starts_with('\'') && raw_val.ends_with('\''))
        || (raw_val.starts_with('"') && raw_val.ends_with('"'))
    {
        if raw_val.len() >= 2 {
            raw_val[1..raw_val.len() - 1].to_string()
        } else {
            String::new()
        }
    } else {
        raw_val.to_string()
    };

    let op = match op_str.as_str() {
        "==" | "=" => ComparisonOperator::Eq,
        "!=" | "<>" => ComparisonOperator::Ne,
        "<=" => ComparisonOperator::Le,
        ">=" => ComparisonOperator::Ge,
        "<" => ComparisonOperator::Lt,
        ">" => ComparisonOperator::Gt,
        "LIKE" => ComparisonOperator::Like,
        _ => return None,
    };

    Some(FilterExpression::Comparison {
        operator: op,
        attribute: field,
        value: val,
    })
}

fn parse_filter_str(trimmed: &str) -> Option<FilterExpression> {
    let upper = trimmed.to_uppercase();
    if upper.contains(" AND ") {
        let parts: Vec<&str> = regex::Regex::new(r"(?i)\s+AND\s+")
            .ok()?
            .split(trimmed)
            .collect();
        let mut list = Vec::new();
        for p in parts {
            if let Some(sub) = parse_single_condition(p) {
                list.push(sub);
            }
        }
        if list.is_empty() {
            None
        } else if list.len() == 1 {
            Some(list.remove(0))
        } else {
            Some(FilterExpression::Logical {
                operator: LogicalOperator::And,
                expressions: list,
            })
        }
    } else if upper.contains(" OR ") {
        let parts: Vec<&str> = regex::Regex::new(r"(?i)\s+OR\s+")
            .ok()?
            .split(trimmed)
            .collect();
        let mut list = Vec::new();
        for p in parts {
            if let Some(sub) = parse_single_condition(p) {
                list.push(sub);
            }
        }
        if list.is_empty() {
            None
        } else if list.len() == 1 {
            Some(list.remove(0))
        } else {
            Some(FilterExpression::Logical {
                operator: LogicalOperator::Or,
                expressions: list,
            })
        }
    } else {
        parse_single_condition(trimmed)
    }
}

pub fn escape_xml(s: &str) -> String {
    s.replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;")
        .replace('"', "&quot;")
        .replace('\'', "&apos;")
}
