# ItemOrderPlan.StartSessionForOrder

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 551-555

```baan
DLL:   cpextrrpapi
This function is available from     2026.01 (KB3606086  ).
Syntax: long ItemOrderPlan.StartSessionForOrder(
domain  cpcom.plnc       iPlanItemScenario,
domain  cpitem           iPlanItem,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
domain  tcpono           iPosition,
domain  tcpono           iSequence,
boolean          iTransferOriginatesFromProductionOrder,
domain  tckotr           iTransactionType,
domain  cpcom.date       iDate,
domain  tccom.bpid       iBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public interfaces works similar to the function
›¼Àœcpcomdll0040.zoom.to.order›¼Àœ .This Public interface opens
the following session based on Order Type.
DOMAIN CONSTANT NAME    ORDER TYPE DESCRIPTION  OPENING SESSION & CODE
tckoor.act.sfc          Production Order        Production Order (tisfc0101m100)
tckoor.act.pur          Purchase Order          Purchase Order Lines
(tdpur4100m900)
tckoor.act.sls          Sales Order             Item Master Plan(cprmp2101m000)
or Special Demand by Item
(cpdsp2100m000)
tckoor.act.sls          Sales Order             Sales Order Lines (tdsls4100m900)
tckoor.cp.sfc           Planned Production Order
Planned Order(cprrp1600m000)
or Capacity Use by
Planned Order (cprrp2100m000)
tckoor.cp.pur           Planned Purchase Order  Planned Order(cprrp1600m000)
or Capacity Use by
Planned Order (cprrp2100m000)
tckoor.act.pur.sched    Purchase Schedule       Purchase Schedule Lines
(tdpur3610m000)
tckoor.act.sls.sched    Sales Schedule          Sales Schedule Lines
(tdsls3611m000)
tckoor.act.pur.adv      Purchase Order Advice   Purchase Order Lines
(tdpur4100m900)
tckoor.act.asc          Assembly Order          Assembly Order(tiasc2100s000)
or Clustered Line Station Orders
(tiasc7530m000)
tckoor.mrp.sls          Forecast                Item Master Plan(cprmp2101m000)
tckoor.mrp.atp          CTP Reservation         CTP Reservations (cprrp0611m000)
tckoor.sls.quot         Sales Quotation         Sales Quotation Lines
(tdsls1501m000)
tckoor.pur.con          Purchase Contract       Purchase Contract Lines
(tdpur3600m000)
tckoor.sls.con          Sales Contract          Sales Contract Lines
(tdsls3600m000)
tckoor.act.srv          Service Order           Service Order Lines
(tssoc2100m100)
tckoor.pss.pur          PRP Purchase Order      Planned PRP Warehouse Order
(tppss6115m000)
tckoor.pss.wrh          PRP Warehouse Order     Planned PRP Warehouse Order
(tppss6115m000)
tckoor.wrh.ass          Warehousing Assembly Order
Warehousing Assembly Orders
(whinh2101m000)
tckoor.act.trf          Warehouse Transfer      Warehousing Order (whinh2100m100)
tckoor.act.pmg          Production Batch        Assembly Part Demand
(cprrp0116m000)
tckoor.srv.planned.act  Planned Activities Service
Planned Activity (tsspc2600m000)
tckoor.cp.ipl           Planned Distribution Order
Planned Order(cprrp1600m000)
or Capacity Use by Planned Order
(cprrp2100m000)
tckoor.cf.ap            Assembly Part Demand    Assembly Part Demand
(cprrp0116m000)
tckoor.act.sfc.man      Production Order (Manual)
Warehousing Order (whinh2100m100)
tckoor.act.pur.man      Purchase Order (Manual) Warehousing Order (whinh2100m100)
tckoor.act.sls.man      Sales Order (Manual)    Warehousing Order (whinh2100m100)
tckoor.act.srv.man      Service Order (Manual)  Warehousing Order (whinh2100m100)
tckoor.act.trf.man      Warehouse Transfer (Manual)
Warehousing Order (whinh2100m100)
tckoor.act.srv.sls      Maintenance Sales Order Maintenance Sales Order
(tsmsc1100m100)
tckoor.act.dpt.wrk      Maintenance Work Order  Work Orders (tswcs2100m100)
tckoor.act.srv.sls.man  Maintenance Sales Order (Manual)
Warehousing Order (whinh2100m100)
tckoor.pur.rfq          Request for Quotation   Request for Quotation Lines
(tdpur1502m000)
tckoor.act.sls.sched.f  Sales Schedule Forecast Sales Schedule Lines
(tdsls3611m000)
tckoor.act.dpt.wrk.man  Maintenance Work Order (Manual)
Warehousing Order (whinh2100m100)
tckoor.stock            Stock                   Warehouse               - Item
Inventory(whwmd2515m000)
tckoor.act.asc.man      Assembly Order (Manual) Warehousing Order (whinh2100m100)
tckoor.epp.quote        Service Quote           Maintenance Sales Quote
(tsepp1100m100)
tckoor.mps.prod         Production Plan         Item Master Plan(cprmp2101m000)
or Critical Material Requirements
(cprmp2505m000)
tckoor.mps.pur          Purchase Plan           Item Master Plan(cprmp2101m000 )
or Critical Material Requirements
(cprmp2505m000)
tckoor.cycle.count      Cycle Counting Order    Cycle Counting Order Lines
(whinh5101m000)
tckoor.adjustment       Adjustment Order        Adjustment Order Lines
(whinh5121m000)
tckoor.apl.asc          Planned Assembly Order  Planned Order (Assembly)
\      (tiapl5636m000)
tckoor.cp.rpt           Planned Production Schedule
Planned Order(cprrp1600m000)
tckoor.product.sched    Production Schedule     Production Schedule Line
(tirpt4602m100)
tckoor.project          Project                 Warehousing Order (whinh2100m100)
tckoor.project.man      Project (Manual)        Warehousing Order (whinh2100m100)
tckoor.enterprise.plan  Warehouse Transfer (Distribution)
Warehousing Order (whinh2100m100)
tckoor.cp.sub           Planned Subcontracting Order
Planned Order (cprrp1600m000)
or Capacity Use by Planned Order
(cprrp2100m000)
tckoor.act.sub.sched    Subcontracting Schedule Purchase Schedule Lines
(tdpur3610m000)
tckoor.exp.supply       Expected Supply         Forecast by Revision to Supplier
(cpvmi0503m100)
tckoor.conf.supply      Confirmed Supply        Forecast by Revision to Supplie
(cpvmi0503m100 )
or Confirmed Supply to Customer
(cpvmi0108m000)
tckoor.bp.forecast      Forecast from Customer  Forecast by Revision from Customer
(cpvmi0506m100)
tckoor.aggr.demand      Forecast to Supplier    Forecast to Supplier
(cpvmi0102m000)
tckoor.bfbp.trf.pur     Buy              -From BP Transfer (Purchase)
Purchase Order Lines
(tdpur4100m900)
tckoor.bfbp.trf.sched   Buy              -From BP Transfer (Schedule)
Purchase Schedule Lines
(tdpur3610m000)
tckoor.stbp.trf.sls     Sold              -To BP Transfer (Sales)
Sales Order Lines (tdsls4100m900)
tckoor.stbp.trf.sched   Sold              -To BP Transfer (Schedule)
Sales Schedule Lines
(tdsls3611m000)
tckoor.stbp.trf.wh.man  Sold              -To BP Transfer (WH Manual)
Warehousing Order (whinh2100m100)
tckoor.stbp.trf.man     Sold              -To BP Transfer (Manual)
Warehousing Order (whinh2100m100)
tckoor.stbp.trf.wh.dis  Sold              -To BP Transfer (WH Distribution)
Warehousing Order (whinh2100m100)
tckoor.cp.cpt           Planned Cost Peg Transfer
Planned Cost Peg Transfers
(cprrp0130m000)
tckoor.act.cpt          Cost Peg Transfer       Cost Peg Transfer (whinh1640m000)
tckoor.proj.contract    Project Contract        Contract (tpctm1600m000)
tckoor.customer.claim   Customer Claim          Customer Claim Lines
(tscmm1600m000)
tckoor.supplier.claim   Supplier Claim          Supplier Claim (tscmm2600m000)
tckoor.quarantine       Quarantine Inventory    Quarantine Inventory Disposition
(whwmd2172m000)
Pre:    N.A.
Post:   N.A.
Input:  iPlanItemScenario       Plan Item Scenario
iPlanItem               Plan Item
iOrderType›¼                                 OrderType
iOrderNumber            Order Number.
iPosition               Position.
iSequence               Sequence Number.
iTransferOriginatesFromProductionOrder
Transfer Originates From Production Order.
iTransactionType        Transaction Type
Mandatory for below Origins
-                                               Production Plan (tckoor.mps.prod)
-                                               Purchase Plan (Purchase Plan)
-                                               Sales Order (Manual) (tckoor.act.sls.man)
-                                               Purchase Order (Manual) (tckoor.act.pur.man)
-                                               Assembly Order (Manual) (tckoor.act.asc.man)
-                                               Production Order (Manual) (tckoor.act.sfc.man)
-                                               Warehouse Transfer (Distribution)
(tckoor.enterprise.plan)
-                                               Sold-To BP Transfer (WH Distribution)
(tckoor.stbp.trf.wh.dis)
-                                               Warehouse Transfer (tckoor.act.trf)
-                                               Sold-To BP Transfer (WH Manual)
(tckoor.stbp.trf.wh.man)
-                                               Warehouse Transfer (Manual) (tckoor.act.trf.man)
-                                               Sold-To BP Transfer (Manual)
(tckoor.stbp.trf.man)
-                                               Service Order (Manual) (tckoor.act.srv.man)
-                                               Maintenance Sales Order (Manual)
(tckoor.act.srv.sls.man)
-                                               Maintenance Work Order (Manual)
(tckoor.act.dpt.wrk.man)
-                                               Project (tckoor.project)
-                                               Project (Manual) (tckoor.project.man)
-                                               Confirmed Supply (tckoor.conf.supply)
iDate                   Date
Mandatory for below Origins
-                                               Forecast to Supplier (tckoor.aggr.demand)
-                                               Expected Supply (tckoor.exp.supply)
-                                               Confirmed Supply (tckoor.conf.supply)
-                                               Forecast from Customer (tckoor.bp.forecast)
-                                               Assembly Part Demand (tckoor.cf.ap)
iBusinessPartner        Business Partner
Mandatory for below Origins
-                                               Forecast to Supplier (tckoor.aggr.demand)
-                                               Expected Supply (tckoor.exp.supply)
-                                               Confirmed Supply (tckoor.conf.supply)
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Public Interface succesfully completed
<> 0                    Otherwise.
```

## Public Interfaces for

## PlanItemExceptionMessageTotal

The following functions are available: PlanItemExceptionMessageTotals.StartOverview
