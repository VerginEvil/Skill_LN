# Considerations on doubles
In the related topics some extra information on double.cmp() is given.
For Baan 4GL engineers it is important to know that:

- A domain is normative for representation of doubles and not for storage in the database

- A double is stored in 52 bits format and with the help of 2x values, so in a combination of 1024, …, 8, …, 1/16, …m m m m, 1/24. This is why doubles are approximate numeric values. The number that approaches the double best is stored.

- In the bshell or debugger a maximum of 6 decimals is shown.

## Remarks
- When problems occur they will mainly occur on comparisons with zero (<param> = 0.0

- Rounding must be done especially before actual update. When comparing intermediate results, you must be careful with rounding (e.g. compare rounded intermediate results with some table field). Advice: round end results only!

- Don't use 'hard coded' tolerances but instead use DD information. For this purpose in Verdi1 the tcmcs.dll0012 DLL was created. It is strongly advised to use this DLL.

## Related topics
- [Reliability of double.cmp()](reliability.of.double.cmp.md)

- [Comparison of doubles in queries](comparison.of.doubles.in.queries.md)
