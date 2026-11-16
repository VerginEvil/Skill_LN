# Numeric constants
The Baan 3GL programming language supports long and floating point constants. Both types can be preceded by a '+' or a '-' sign.

## Long constants
A long constant can be specified in decimal notation or in hexadecimal notation. Only non-negative values can be specified. A preceding minus sign is not part of the constant, but is considered as a separate unary or binary minus operator.
Notice that the concept of constants is a feature of the bic compiler. The compiler does not support long constants outside the signed 32-bit value range. The object code produced by the compiler will be executed by the bshell.
The bshell may run in [32-bit mode](data_types.md#Long32) or in [64-bit mode](data_types.md#Long64). The bic compiler does not have any special support for the [64-bit mode](data_types.md#Long64) of the bshell. In fact the compiler produces the same code as it always produced for bshell versions which did not distinguish between [32-bit mode](data_types.md#Long32) and [64-bit mode](data_types.md#Long64). Therefore, the compiler does not support long constants outside the signed 32-bit value range.
When using the decimal notation, the allowed value range is the non-negative signed 32-bit value range: [0 … 2^31 - 1]. When immediately preceded by a minus sign, also the value 2^31 is allowed. For example:
```

0
1
10
2147483647
2147483648	| Error: Long constant '2147483648' too large (MAX 2147483647).
-2147483648
-2147483649	| Error: Long constant '-2147483649' too large (MAX -2147483648).
0 - 2147483648
0 - 2147483649	| Error: Long constant '-2147483649' too large (MAX -2147483648).
```
When using the hexadecimal notation, the allowed range is the same as when using the decimal notation, but now there is no exception when immediately preceded by a minus sign. For example:
```

0x0
0X1
0x7fffffff
0x7FFFFFFFF
0x800000000	| Error: Hexadecimal constant: '80000000' cannot be converted to long.
-0x7FFFFFFFF
-0x800000000	| Error: Hexadecimal constant: '80000000' cannot be converted to long.
```

## Floating point constants
Floating point constants consist of the digits 0-9 and a decimal point. You cannot end a constant with a decimal point. An exponential part can be added to a constant by including the letter 'e' followed by a long constant (maximum 307). You can have up to six digits after the decimal point in a constant. For example:
```

123.56
0.8743
.8743
123.5e-5
-2.34e10
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Constants](constants.md)
