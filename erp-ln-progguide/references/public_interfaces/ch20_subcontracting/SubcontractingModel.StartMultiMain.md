# SubcontractingModel.StartMultiMain

> Chapter: Chapter 20 Public Interfaces for Subcontracting
>
> Group: Public Interfaces for SubcontractingModel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 835-837

```baan
DLL:   tiextsubapi
This function is available from     2025.03 (KB3543995  ).
Syntax: long SubcontractingModel.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iProductionSite,
domain  tcitem           iProduct,
domain  tccom.bpid       iSubcontractor,
domain  tcsite           iSubcontractorSite,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tirpt.revi       iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi Main session
ProductSubcontractingModel(tisub1600m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -                 The parent session is blocked
until the child session exits.
The session will be started as a
zoom session.
MODELESS                               -              Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter                    Not used.
iSessionIndex
Session Index.
Possible (standard) values are:
when Sites concept is active :
1                               -                     Session is sorted using Product.
3                               -                     Session is sorted using Product Site.
5                               -                     Session is sorted using Suncontractor.
when Sites concept is not active :
1                               -                     Session is sorted using Product.
iQueryExtend                    A specific query to be used when
zooming to this session. Optional.
iProductionSite                 Production Site                       - Mandatory only
if sites concept is active.
iProduct                        Product                       - Mandatory
iSubcontractor                  Subcontractor                       - Optional
iSubcontractorSite              Subcontractor Site                       - Optional
iShipFromBusinessPartner        Ship From Business Partner                       - Optional
iRevision                       Revision                       - Optional
Output: oExceptionMessage               The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                    An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                               Session started.
<> 0                            Error Occurred.
```
