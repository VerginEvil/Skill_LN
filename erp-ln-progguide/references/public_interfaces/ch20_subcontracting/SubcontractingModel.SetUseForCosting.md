# SubcontractingModel.SetUseForCosting

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 833-834

```baan
DLL:   tiextsubapi
This function is available from     2023.04 (KB2282924  ).
Syntax: long SubcontractingModel.SetUseForCosting(
domain  tcsite           iProductionSite,
domain  tcitem           iProduct,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to set the Use for Costing flag for a
Subcontracting Model.
For all Subcontracting Model›¼À                      ™s revisions for this Product and
Site, the use for Costing flag will be set.
For all other Subcontracting Models related to this Product and
Site, the Use for Costing flag will be cleared.
This function follows the same logic as the form command
›¼ÀœUse for Costing›¼À                       in session Product Subcontracting List
(tisub1100m000).
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
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Use for Costing flag has been set.
<> 0                    The Use for Costing flag has not been
set.
```
