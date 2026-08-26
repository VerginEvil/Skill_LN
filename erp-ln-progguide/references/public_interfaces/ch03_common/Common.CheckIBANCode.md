# Common.CheckIBANCode

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 96-97

```baan
DLL:   tcextcomapi
This function is available from     2023.11 (KB2300545  ).
Syntax: long Common.CheckIBANCode(
domain  tccom.iban       iIBANCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl. : This function checks if the ibancode is OK
The following steps are performed:
1.      Determine the country (position 1 and 2 from
i.iban.code). If the country code is not a valid
ISO                              -3166 country code, then the IBAN code is
not correct.
2.      Determine the length of the IBAN code based on
the country code. If the length of i.iban.code
is not the same, then the IBAN code is not
correct.
3.      Validate the IBAN code:
a.      Move characters on position 1                              -4
(country code + check digit) to the
utmost right position.
b.      Replace alphanumeric characters by
numerics (A = 10, B= 11, ..., Z = 35).
If one of the characters is not valid,
then the IBAN code is not orrect.
c.      If ( resulting number                               \ 97 ) = 1, then
the IBAN code is correct. Otherwise the
IBAN code is not correct.
Some examples of IBAN numbers
FR1420041010050500013M02606
GR1601101250000000012300695
IS140159260076545510730339
IE29AIBK93115212345678
IT40S0542811101000000123456
PL27114020040000300201355387
PT50000201231234567890154
ES9121000418450200051332
SE3550000000054910000003
GB29NWBK60161331926819
AD1200012030200359100100
CZ6508000000192000145399
TR330006100519786457841326
TR560006100000012990022302
TR260007100101301030077EUR (from internet)
BG80BNBG96611020345678
Pre.  : NA
Post  : NA
Input : iIBANCode :             The ibancode which has to be checked
(mandatory)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - IBAN Code is correct
<> 0                                          - Otherwise
```
