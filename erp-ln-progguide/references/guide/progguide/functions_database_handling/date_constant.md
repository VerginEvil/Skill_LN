# Date constant
The date constant specifies a date value.

## Syntax
```

<date constant>
    ::= DATE '<year>-<month>-<day>'
      | DATE "<year>-<month>-<day>"

<year>    ::= <digit>...
<month>   ::= <digit>...
<day>     ::= <digit>...
```

## Syntactical restrictions
The date represented by the date literal must be a valid date according to the Gregorian calender. The value of the month must lie in the range [1..12]. The value of the day must lie in the range [1..31]. The minimum date constant is "0001-01-01"; the maximum date constant is "9999-12-31".

## Semantics
The data type of a date constant is *date*.

## Examples
The following date constant represents the date January 10, 2003.
```

DATE '2003-1-10'
```
The following date constant represents the date March 10, 1. That is, the year 1.
```

DATE '1-03-10'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
