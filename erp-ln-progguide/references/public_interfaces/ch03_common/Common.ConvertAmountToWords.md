# Common.ConvertAmountToWords

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 98-99

```baan
DLL:   tcextmcsapi
This function is available from     2023.01 (KB2274799  ).
Syntax: long Common.ConvertAmountToWords(
domain  tcamnt           iAmount,
domain  tclang           iSystemLanguage,
ref     domain  tcmcs.s130m      oAmountInWordsBeforeDecimalSign mb,
ref     domain  tcmcs.st65m      oAmountInWordsAfterDecimalSign mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:     Expl:      This function converts an amount into words in the given
language.
Pre:       NA
Post:      NA
Input:     iAmount                            - Amount to be converted into written text
iSystemLanguage                               - SystemLanguage in which
oAmountInWordsBeforeDecimalSign
and oAmountInWordsAfterDecimalSign must
be expressed.(mandatory)
Output:    oAmountInWordsBeforeDecimalSign
-                                               iAmount before decimal sign in written text
oAmountInWordsAfterDecimalSign
-                                               iAmount after decimal sign in written text
NOTE: For the most languages the decimals
are written in digits. Like: 'und 43/100'
for German. Only if there is a legal
requirement for a language,
decimals are written in words.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                                             - iAmount is converted into words.
<> 0                                          - on Errors
```
