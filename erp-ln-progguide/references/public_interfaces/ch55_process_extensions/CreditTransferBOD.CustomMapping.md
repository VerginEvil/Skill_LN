# CreditTransferBOD.CustomMapping

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CreditTransferBOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1995-1996

Define custom mapping for CreditTransferBOD elements. This process extension is available from 2025.03 ( KB3555913 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to set a customer determined
value for some elements of the CreditTranserBOD, other than the
defaulted value based on LN logic .
```

To implement this process extension, you need to implement the following method(s):

## tcext.bod0002.get.credittransferheader.forwardingagentpa

## rty.clearingsystemmemberid

```baan
Syntax: long tcext.bod0002.get.credittransferheader.forwardingagentparty.clearingsystemmemberid(
domain  tfgld.btno       i.payment.batch,
domain  tfcmg.bank       i.bank,
domain  tfcmg.paym       i.payment.method,
domain  tcmcs.str25      i.ln.stnd.id.value,
ref     domain  tcmcs.str25      o.clearingsystemmemberid )
Usage:        Use this method to program the custom logic that defines the content
of the CreditTransferHeader/ForwardingAgentParty/ClearingSystemMemberID
element in the CreditTransferBOD.
Input:
-               i.payment.batch       - the Payment Batch for which the CreditTransferBOD
is published (tfcmg103.btno)
-               i.bank                - the Bank Relation of the BOD (tfcmg103.bank)
-               i.payment.method      - the Payment Method of the BOD (tfcmg103.paym)
-               i.ln.stnd.id.value    - the standard LN value for the
ClearingSystemMemberID element
Output:
-               o.clearingsystemmemberid - the value to be published in the BOD element.
return an empty value if the standard LN
logic should be used.
return:
-               0                 - OK
-               DALHOOKERROR      - not OK
```

## Process Extensions for CycleCountingData

The following process extension(s) is/are available: CycleCountingData.SkipDelete
