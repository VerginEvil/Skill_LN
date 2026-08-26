# SubcontractingModel.ApproveRevision

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 830-831

```baan
DLL:   tiextsubapi
This function is available from     2023.04 (KB2282924  ).
Syntax: long SubcontractingModel.ApproveRevision(
domain  tcsite           iProductionSite,
domain  tcitem           iProduct,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tirpt.revi       iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to Approve a Subcontracting Model
Revision.
The functionality is the same as the Form Command
"Approve Revision" in session in session Product Subcontracting
List (tisub1100m000).
This Public Interface can only be used if the Sites concept is
active.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
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
Return: 0                       The Subcontracting Model Revision has
been approved.
<> 0                    The Subcontracting Model Revision has
not been approved.
```
