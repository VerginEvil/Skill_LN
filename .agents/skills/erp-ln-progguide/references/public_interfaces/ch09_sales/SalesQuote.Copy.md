# SalesQuote.Copy

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 290-292

```baan
DLL:   tdextslsapi
This function is available from 2023.05 (KB2284499).
Syntax: long SalesQuote.Copy(
domain  tcqono           iSourceQuotation,
domain  tcqono           iTargetQuotation,
domain  tccom.bpid       iTargetSoldToBp,
domain  tccwoc           iTargetSalesOffice,
domain  tccotp           iTargetOrderType,
domain  tcdate           iTargetPlannedDeliveryDate,
domain  tcyesno          iCopyFromHistory,
domain  tcyesno          iCopyAllLines,
domain  tcyesno          iCopyAlternatives,
domain  tcyesno          iCopyBomComponents,
domain  tcyesno          iCopyMissedLines,
domain  tcyesno          iCopyMaterialPriceInformation,
domain  tcyesno          iCopyAfterSalesService,
domain  tcyesno          iCopyProjectPegs,
domain  tcyesno          iCopyTexts,
domain  tcyesno          iCalculateNewPriceAndDiscounts,
long             iNrOfLinesToAdd,
const   domain  tcpono           iOriginalLineArray(),
const   domain  tdsls.altn       iOriginalAlternativeArray(),
ref     domain  tcqono           oCopiedToQuotation,
ref             long             oNrOfQuoteLinesAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function copies the given quotation to a new quotation or
the lines to an existing quotation.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSourceQuotation        - The quotation from which the copy will
be done. Mandatory.
iTargetQuotation        - The series of a new quotation or
an existing quotation to were the
lines are will copied to. Mandatory.
iTargetSoldToBp         - The Sold-to Business Partner for
the new quotation. Mandatory.
iTargetSalesOffice      - The Sales Office for the new
quotation. Mandatory.
iTargetOrderType        - The Sales Order Type for the new
quotation. Mandatory.
iTargetPlannedDeliveryDate      - The Planned Delivery Date for
the new quotation. Mandatory.
iCopyFromHistory        - Yes: Copies from the sales quotation
history table.
No:  Copies from the actual sales
quotation table.
iCopyAllLines           - Yes: All lines will be copied.
No:  Not all lines are copied a
selection of line must be given via
the variables:
- i.nr.of.lines.to.add
- i.original.line.array
- i.original.alternative.array
iCopyAlternatives       - Yes: Alternative lines will be copied.
No:  Alternative lines are not copied.
iCopyBomComponents      - Yes: BOM components are copied from
the source line.
No:  BOM components are not copied but
determined again from master data.
iCopyMissedLines        - Yes: Missed lines will be copied.
No:  Missed lines are not copied.
iCopyMaterialPriceInformation   - Yes: Material price
information is copied from the source
line.
No:  Material price
information is not copied but
determined again from master data.
iCopyAfterSalesService  - Yes: After sales service lines
will be copied.
No:  After sales service lines are
not copied..
iCopyProjectPegs        - Yes: Project peg is copied.
No:  Project peg is not copied.
iCopyTexts              - Yes: Text is copied.
No:  Text is not copied.
iCalculateNewPriceAndDiscounts  - Yes: Price and
discount are recalculated.
No:  Price and
discount are not recalculated.
iNrOfLinesToAdd - The number of lines that are to be
copied to the sales quotation.
This argument can be set to 0 if
i.copy.all.lines = Yes.
iOriginalLineArray      - The line numbers of the original
quotation lines that will be copied.
The number of entries in this array
must be equal to i.nr.of.lines.to.add.
This array is allowed to be empty if
i.copy.all.lines = Yes.
iOriginalAlternativeArray       - The alternative numbers of the
original quotation lines that will be
copied.
The number of entries in this array
must be equal to i.nr.of.lines.to.add.
This array is allowed to be empty if
i.copy.all.lines = Yes.
Output: oCopiedToQuotation      - The new or existing quotation were
the lines are added.
oNrOfQuoteLinesAdded    - The number of lines added to
the quotation.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Copy was successful
<> 0                    - An error occurred
```
