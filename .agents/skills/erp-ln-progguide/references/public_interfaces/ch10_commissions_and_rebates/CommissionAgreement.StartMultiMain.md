# CommissionAgreement.StartMultiMain

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for CommissionAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 392-393

```baan
DLL:   tdextcmsapi
This function is available from 2026.08 (KB3682830).
Syntax: long CommissionAgreement.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iRelation,
domain  tcyesno          iChildAgreement,
domain  tdcms.agrp       iAgreementGroup,
domain  tccprj           iProject,
domain  tcitem           iItem,
domain  tdcms.cmgp       iCommissionRebateGroup,
domain  tcdate           iEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function starts the Multi-Main session Commission Agreement
(tdcms0635m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used.
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iSoldToBusinessPartner  Sold-to Business Partner (Optional)
iRelation               Relation (Optional)
iChildAgreement         Child Agreement (Yes/No) (Mandatory)
iAgreementGroup         Agreement Group (Optional)
iProject                Project (Optional)
iItem                   Item (Optional)
iCommissionRebateGroup  Commission/Rebate Group (Optional)
iEffectiveDate          Effective Date (Mandatory)
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these can be retrieved using
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the Exception
functions to get all relevant
information.
Return: 0                       Session started.
<> 0                    An error has occurred.
```
