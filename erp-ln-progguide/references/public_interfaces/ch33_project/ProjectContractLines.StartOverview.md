# ProjectContractLines.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractLines
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1702-1703

```baan
DLL:   tpextctmapi
This function is available from 2024.07 (KB2329416).
Syntax: long ProjectContractLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tccono           iProjectContract,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iInvoiceToBusinessPartner,
ref     domain  tccono           oContract,
ref     domain  tpctm.cnln       oContractLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session "Contract Lines"
(tpctm1110m000) for a Contract or Project.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used
iSessionIndex           Specifies the session index that is to be used.
Please
be aware that the iStartFilter will overrule the
index
passed in this argument. So when not using a
startfilter
the session index will match the value of this
variable.
iQueryExtend            A specific query to be used when zooming to this
session.
iProject                Project. Optional
iProjectContract        Project Contract. Optional
iSoldToBusinessPartner  Sold to Business Partner. Optional
iInvoiceToBusinessPartner
Invoice To Business Partner. Optional
Output: for iStartMode MODAL:
oContract       The selected Contract
oContractLine   The selected Contract Line
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
