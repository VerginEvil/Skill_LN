# PurchaseRequisitionLine.ConvertToPurchaseRFQ

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisitionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 420-422

```baan
DLL:   tdextpurapi
This function is available from     2021.05 (KB2185794  ).
Syntax: long PurchaseRequisitionLine.ConvertToPurchaseRFQ(
domain  tcrqno           iPurchaseRequisition,
domain  tcpono           iRequisitionLine,
domain  tcyesno          iAddToExistingRFQ,
domain  tcqono           iExistingRFQ,
domain  tcseri           iRFQSeries,
domain  tcrfq.type       iRFQType,
domain  tcqono           iPreviousRFQ,
ref     domain  tcqono           oGeneratedRFQ,
ref     domain  tcpono           oGeneratedRFQLine,
ref     domain  tcpono           oGeneratedRFQSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts the given requisition line to a purchase
RFQ. Conversion is only allowed if the requisition header has
the proper status (i.e. Approved or In Process), and the
requisition line is not rejected. The Conversion Type of the
requisition line must be 'RFQ'.
Pre:    Caller must set a retry              -point
Post:   Caller must commit or abort the transaction.
Input:  iPurchaseRequisition                  - Requisition; Mandatory
iRequisitionLine                              - Requisition Line; Mandatory
iAddToExistingRFQ                             - Yes: the requisition line is converted
to an existing RFQ. Use iExistingRFQ
to indicate to which RFQ the
requisition line must be added.
Notes:
* this will override the value
that is passed in iPreviousRFQ.
* this option is only allowed if
the concept of
'Enhanced Line Handling' is
used for the given RFQ.
No: this option allows a more regular
form of commingling. Several
requisition lines can be converted
to one (or more) RFQ's, but only
if the passed RFQ matches the data
on the requisition line.
See explanation at 'iPreviousRFQ'.
iExistingRFQ                                  - Indicates the RFQ to which the given
requisition line must be converted.
This field is mandatory if
iAddToExistingRFQ is Yes. The field
must be empty if iAddToExistingRFQ
is No.
iRFQSeries                                    - The RFQ series that will be used when
a new RFQ is generated.
iRFQType                                      - The RFQ Type that will be used when
a new RFQ is generated.
iPreviousRFQ                                  - If filled, the function tries to add
a requisition line to that RFQ. If they
do not match, then a new RFQ is
generated. Filling this field can be done
when calling this function multiple
times in order to convert multiple
requisition lines to one (or: as little
as possible) RFQs.
If maximal commingling must be obtained,
then the order in which the requisition
lines are converted is important.
Output: oGeneratedRFQ                         - The generated RFQ
oGeneratedRFQLine                             - The generated RFQ line
oGeneratedRFQSequence                         - The generated RFQ sequence
Return: 0                                     - The requisition line is converted
<> 0                                          - An error occurred
```
