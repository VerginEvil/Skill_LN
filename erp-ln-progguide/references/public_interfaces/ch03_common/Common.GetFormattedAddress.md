# Common.GetFormattedAddress

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 110-111

```baan
DLL:   tcextcomapi
Syntax: long Common.GetFormattedAddress(
domain  tccom.cadr       iAddress,
long             iNumberOfLines,
domain  tcccty           iFromCountry,
ref             string           oFormattedAddress(,) fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This functions formats an given addresscode into a
formatted address array of a given number of lines.
Pre:    iAddress must exists in tccom130
Multibyte Array used for oFormattedAddress must be
declared and initialized.
Post:   NA
Input:
iAddress                - The address code for which the
formatted address must be generated.
(mandatory)
iNumberOfLines          - The maximum number of lines of the
formatted address.(mandatory)
iFromCountry            - When iFromCountry is filled,
the country information will
only be used in the formated
address when it differs from
iFromCountry.
When left empty always the country
information is used in the formated
address.
|*Example       if i.from.country = "NLD" the Dutch addresses will not have
country information in the formatted address. This can be used
when a company located in "NLD" sends invoices or mailings to
addresses in "NLD".
Moonen Shipyards BV
Kade 35
1780 AA Den Helder
The addresses outside "NLD" will have country information in
the formatted address:
Moonen F?›¼•¼?›¼•Ã?›¼•¼?›¼•¶rdertechnik GmbH
Balhorner Feld 1
33106 Paderborn
Deutschland
if i.from.country = empty both addresses will have country
information in the formatted address:
Moonen Shipyards BV
Kade 35
1780 AA Den Helder
Nederland
Moonen F?›¼•¼?›¼•Ã?›¼•¼?›¼•¶rdertechnik GmbH
Balhorner Feld 1
33106 Paderborn
Deutschland
-
Output: oFormattedAddress       - Array with formatted address lines.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                       - Formatted address is returned
<> 0                    - on errors
```
