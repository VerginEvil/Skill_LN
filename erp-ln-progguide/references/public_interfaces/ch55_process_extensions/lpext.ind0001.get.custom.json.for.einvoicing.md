# lpext.ind0001.get.custom.json.for.einvoicing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IND.EInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2053-2054

```baan
Syntax: long lpext.ind0001.get.custom.json.for.einvoicing(
domain  tcncmp           i.financial.company,
domain  tctran           i.transaction.type,
domain  tcgld.docn       i.invoice.number,
long             i.json,
ref             long             o.json )
Usage:        Expl:   Use this method to get the generated JSON and to modify it
i.json will be the output JSON after user does the changes
i.json can be copied to a local variable with Json.copy function
and after the changes are done, the value can be written to
o.json varialble via JSON.COPY function
For reading and editing JSON file
For Eg.
"DocDtls": {
"Typ": "TST",
"No": "TEST123454",
"Dt": "24/06/2025"
},
To read the value from the JSON
inv.number = JSON.getString( i.json,"No")
To update the value
JSON.setString( i.json,"No","NewValue")
Pre:    NA
Post:   NA
Input:  i.financial.company -> Financial Company
i.transaction.type -> Transaction type
i.invoice.number -> Invoice Number
i.json -Generated JSON for IRN
Output: o.json - User Edited JSON
Return: 0       -       Success
DALHOOKERROR    - Otherwise.
```
