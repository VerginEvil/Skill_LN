# tfext.acp0001.set.custom.composing.fields

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseSelfBilledInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2191-2192

```baan
Syntax: long tfext.acp0001.set.custom.composing.fields(
ref             string           o.composing.fields() )
Usage:        Expl:
Use this method in order to use a Custom Compose Criteria for
the Self                      -Billing Method.
If an implementation of this method is done, and the string with
composing fields is filled, and this method is returning 0,
then in the Self                      -Billing Method (tcmcs0157m000) session
the Compose Criteria (tcmcs057.cmpc) field can be set
as Custom Compose.
Via this method, one or more fields can be defined in a
(comma separated) string. Those defined fields will be
used as composing criteria for creating the Purchase
Self                      -Billed Invoice in the Purchase Self-Billing
(tfacp2290m000) process.
In the Custom Compose flow, the standard Self                      -Billing will use
the below pre                      -defined fields already for composing the
Purchase Self                      -Billed Invoice (as these are invoice header
attributes):
tfacp240.ifbp,
tfacp240.otbp,
tfacp240.ccur,
tfacp240.vatc,
tfacp240.ptyp,
tfacp240.rtyp,
tfacp240.mcfr
So, via this method, EXTRA composing attributes can be defined.
Note that only attributes of below tables may be used:
-                               Order Data for Approval (tfacp240)
-                               Purchase Consumptions (tfacp249)
Also Customer Defined Fields (CDF), added to the above mentioned
tables (tfacp240 and tfacp249), can be used as extra composing
fields.
EXAMPLE:
If the composing must also be done on Receipt (tfacp249.rcno)
and an own CDF field (tfacp249.cdf_0001), this method
should return:
o.composing.fields = "tfacp249.rcno, tfacp249.cdf_0001"
return(0)
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.composing.fields                    - String with composing composing
fields (comma separated)
Maximum string length is 500 (sb).
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in setting
the composing fields.
```

## Process Extensions for QualityFailureDocument

The following process extension(s) is/are available: QualityFailureDocument.SkipPrint
