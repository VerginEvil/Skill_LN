# SubcontractingModel.CreateNewRevision

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 841-842

```baan
DLL:   tiextsubapi
This function is available from 2025.01 (KB3528275).
Syntax: long SubcontractingModel.CreateNewRevision(
domain  tcsite           iProductionSite,
domain  tcitem           iProduct,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tirpt.revi       iRevision,
ref     domain  tirpt.revi       oNewRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to create a new Subcontracting Model
Revision based on an existing Subcontracting Model Revision.
The functionality is the same as the Form Command
"New Revision" in session in session Product Subcontracting
List (tisub1100m000).
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iProductionSite         -       Production Site (Mandatory if
the Site concept is active).
iProduct                -       Product (Mandatory)
iSubcontractor          -       Subcontractor (Mandatory)
iSubcontractorSite      -       Subcontractor Site.
(Mandatory if the Resource by
Site conept is active)
iShipFromBusinessPartner-       Ship From Business Partner.
(Mandatory if Resource by Site
is not active, derived from
iSubcontractorSite otherwise).
iRevision               -       The original revision(Optional).
If not provided, the latest
revision of the Subcontracting
Model is used.
Output: oNewRevision            -       The created Revision.
oExceptionMessage               The last message if any message
is found. If more than one
message is given, these are
present in the oExceptionID.
oExceptionID                    An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return:   0                     -       New Revision successfully
created.
<>0                     -       Otherwise.
```
