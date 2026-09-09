# CustomerClaimLine.CalculateClaimAmount

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1544-1546

```baan
DLL:   tsextcmmapi
This function is available from 2024.12 (KB3543998).
Syntax: long CustomerClaimLine.CalculateClaimAmount(
long             iProcessingOptionSet,
ref     domain  tcamnt           oClaimAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this function to determine the default Claim Amount for the
Claim Line.
Pre:    Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
Claim                   domain  tcorno          empty
The Customer Claim to calculate a Claim Amount for.
(mandatory)
ClaimLine               domain  tcpono          0
The Claim Line to calculate a Claim Amount for.
Mandatory when UseClaimLineData is Yes.
Claim Line
UseClaimLineData        domain  tcyesno         tcyesno.yes
Use Claim Line Data;
when Yes, the data of the passed Claim Line is
retrieved and used for the calculation. In this case,
ClaimLine is mandatory.
When No, the Claim Line is ignored and the data passed
via iProcessingOptionSet is used. In this way a
simulated Claim Amount can be calculated.
CostType                domain  tsmdm.cotp      tsmdm.cotp.material
Cost Type (tscmm110.cotp)
ClaimMethod             domain  tscmm.clmt      tscmm.clmt.costs
Claim Method (tscmm110.clmt)
ServiceType             domain  tsmdm.cstp      empty
Service Type (tscmm110.cstp)
Item                    domain  tcitem          empty
Item (tscmm110.item)
SerialNumber            domain  tcibd.sern      empty
Serial Number (tscmm110.sern)
LaborRateCode           domain  tcppl.clrt      empty
Labor Rate Code (tscmm110.clrt)
LaborType               domain  tcckow          empty
Labor Type (tscmm110.chlt)
TravelSpecificationType domain  tssoc.tspt      tssoc.tspt.not.app
Travel Specification Type (tscmm110.tspt)
CostComponent           domain  tccpcp          empty
Cost Component (tscmm110.ccmp)
ClaimedQuantity         domain  tsmdm.qmat      0.0
Claimed Quantity (tscmm110.qccl)
QuantityUnit            domain  tccuni          empty
Quantity Unit of Claimed Quantity (tscmm110.cucq)
ConvFactQtyUnit         domain  tcconv          1.0
Conversion Factor of Claimed Quantity Unit
(tscmm110.cvcq)
Output: oClaimAmount
The Claim Amount expressed in the Claim Currency.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0
No Error and the Claim Amount is returned.
<> 0
Error situation.
```
