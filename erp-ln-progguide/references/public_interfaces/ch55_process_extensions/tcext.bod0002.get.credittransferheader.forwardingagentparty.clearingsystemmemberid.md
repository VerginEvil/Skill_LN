# tcext.bod0002.get.credittransferheader.forwardingagentparty.clearingsystemmemberid

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CreditTransferBOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2015-2015

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
- i.payment.batch       - the Payment Batch for which the CreditTransferBOD
is published (tfcmg103.btno)
- i.bank                - the Bank Relation of the BOD (tfcmg103.bank)
- i.payment.method      - the Payment Method of the BOD (tfcmg103.paym)
- i.ln.stnd.id.value    - the standard LN value for the
ClearingSystemMemberID element
Output:
- o.clearingsystemmemberid - the value to be published in the BOD element.
return an empty value if the standard LN
logic should be used.
return:
- 0                 - OK
- DALHOOKERROR      - not OK
```
