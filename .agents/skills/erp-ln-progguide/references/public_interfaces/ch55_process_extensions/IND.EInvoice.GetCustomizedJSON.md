# IND.EInvoice.GetCustomizedJSON

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IND.EInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2053-2053

```baan
Determine custom JSON for IRN.
This process extension is available from 2025.08 (KB3610568).
Technical information for this process extension:
Usage:        With this Process Extension, it is possible to edit the JSON  used in
IRN Process if required
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
To implement this process extension, you need to implement the following method(s):
```
