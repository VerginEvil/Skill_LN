# ServiceOrder.UnpackObjectReference

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1448-1449

```baan
DLL:   tsextsocapi
This function is available from 2025.04 (KB3568308).
Syntax: long ServiceOrder.UnpackObjectReference(
domain  tcborf           iObjectReference,
ref     domain  tcpono           oLine,
ref     domain  tsmdm.cotp       oCostType,
ref     domain  tcnins           oInstallment,
ref     domain  tcsli.ninl       oInstallmentLine,
ref     domain  tctax.indi       oTaxIndicator,
ref     domain  tcpono           oActualResourceSequence,
ref     domain  tcpono           oInvoiceLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function unpacks the reference string to Line number,
and Cost Type.
Note:
if oCostType = tsmdm.cotp.all then oLine is an
activity number.
if oCostType  <> tsmdm.cotp.all then oLine is a
cost line number.
Pre:    -
Post:   -
Input:  iObjectReference        - Object Reference; Mandatory
Output: oLine                   - Line number or Activity line
oCostType               - Cost Type
oInstallment            - Installment
oInstallmentLine        - Installment Line
oTaxIndicator           - Tax Indicator
oActualResourceSequence - Actual Resource Sequence
oInvoiceLineSequence    - Invoice Line Sequence
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation.
Return: 0       - No Error, and the object reference could be
unpacked correctly.
<> 0    - Error, and the object reference could not be
unpacked correctly.
```
