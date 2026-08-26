# Tax.CalculateTaxBaseAmount

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1621-1621

```baan
DLL:   tcexttaxapi
This function is available from     2025.04 (KB3566846  ).
Syntax: long Tax.CalculateTaxBaseAmount(
domain  tctax.tbvf       iTaxBaseValueFormula fixed,
domain  tcamnt           iAmount,
ref     domain  tcamnt           oTaxBaseAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the tax base value amount.
With the formula code the formula is read in table
'Tax Base Value Formulas' (tctax011).
The amount is put in the formula at the place where a
tax base value variable is used with the
'Tax Base Value Type' = 'Goods Amount' or 'Labor Amount'.
Pre:    N/A
Post:   N/A
Input:
iTaxBaseValueFormula                          - The tax base value formula code.
Mandatory.
iAmount                                       - The net amount or labor amount based
on the amount type used in the formula.
Optional.
Output:
oTaxBaseAmount                                - The tax base amount.
oExceptionMessage                             - The last message if any message is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID                                  - An ID that refers to the exception information.
Use the functions in Exception to get
all relevant information.
Return:
0                                             - Tax base value amount successfully calculated.
<> 0                                          - Error.
```
