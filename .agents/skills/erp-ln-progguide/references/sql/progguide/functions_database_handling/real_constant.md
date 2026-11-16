# Real constant
The real constant specifies a real (approximate numeric) value.

## Syntax
```

<real constant>
    ::= [-]<mantissa>[<exponent>]

<mantissa>
    ::= <unsigned integer>.<unsigned integer>
      | .<unsigned integer>

<exponent>
    ::= e[-|+]<unsigned integer>

<unsigned integer>
    ::= <digit>...
```

## Syntactical restrictions
The value of the real constant must lie in one of the following ranges.

- `[ –1.7976931348623157e+308.. –4.94065645841246544e–324 ]`

- `[ 0.0 ]`

- `[ 4.94065645841246544e–324.. 1.7976931348623157e+308 ]`

## Semantics
The type of a real constant is *real*. The value is the closest approximate numeric value representing the real constant.

## Examples
```

123.456
–.25
1.0e-16
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
