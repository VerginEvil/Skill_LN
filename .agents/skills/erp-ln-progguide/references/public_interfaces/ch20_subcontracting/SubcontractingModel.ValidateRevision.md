# SubcontractingModel.ValidateRevision

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 847-847

```baan
DLL:   tiextsubapi
This function is available from 2023.04 (KB2282924).
Syntax: long SubcontractingModel.ValidateRevision(
domain  tcsite           iProductionSite,
domain  tcitem           iProduct,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tirpt.revi       iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to Validate a Subcontracting Model
Revision.
All validation messages will be returned in
oExceptionID. It can be filled with non-blocking information or
warning messages while the revision is valid. Messages can also
be returned if the return value is 0.
The validation is identical to that of session Validate Product
Subcontracting Models (tisub1200m000).
This Public Interface can only be used if the Sites concept is
active.
Pre:    -
Post:   -
Input:  iProductionSite         Site (mandatory).
iProduct                Product (mandatory).
iSubcontractor          Subcontractor (mandatory).
iSubcontractorSite      Subcontractor Site (mandatory
if Resource by Site is active).
iShipFromBusinessPartner
Ship From Business Partner (mandatory
if Resource by Site is not active,
derived from iSubcontractorSite
otherwise).
iRevision               Subcontracting Model Revision
(mandatory).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Subcontracting Model Revision is
valid. Non-blocking messages can still
be returned.
<> 0                    The Subcontracting Model Revision is
not valid.
```
