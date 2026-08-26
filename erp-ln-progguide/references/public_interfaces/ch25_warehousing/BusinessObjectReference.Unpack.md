# BusinessObjectReference.Unpack

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for BusinessObjectReference
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1307-1308

```baan
DLL:   whextinhapi
This function is available from     2025.04 (KB3568308  ).
Syntax: long BusinessObjectReference.Unpack(
domain  tcborf           iObjectReference,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  whinh.oorg       oOrderOrigin,
ref             boolean          oInternalOwnership,
ref     domain  tccom.bpid       oOwner,
ref     domain  tcpono           oLandedCostsLine,
ref     domain  whinh.shpm       oReceipt,
ref     domain  tcpono           oReceiptLine,
ref     domain  tcpono           oPegLine,
ref     domain  tcpono           oBomLine,
ref     domain  tcwset           oOrderSet,
ref     domain  whinh.orders     oOrderIndicator,
ref     domain  tcvar.orig       oVarianceOrigin,
ref     domain  tctax.indi       oTaxIndicator,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   The function unpacks the reference string.
Input:  iObjectReference               - Object Reference (Mandatory)
Output: oOrderLine                            - Order line
oOrderSequence                                - Order Sequence
oOrderOrigin                                  - Order Origin
oInternalOwnership                            - Internal Ownership Indicator
oOwner                                        - Owner
oLandedCostsLine                              - Landed Costs Line
oReceipt                                      - Receipt
oReceiptLine                                  - Receipt Line
oPegLine                                      - Peg Line
oBomLine                                      - BOM Line
oOrderSet                                     - Order Set
oOrderIndicator                               - Order Indicator (only used for General
Ledger)
oVarianceOrigin                               - Variance Origin
oTaxIndicator                                 - Tax Indicator
Return: 0: ok, <> 0: Error
```

## Public Interfaces for PrepackingAdvice

The following functions are available: PrepackingAdvice.Create PrepackingAdvice.GenerateProposal PrepackingAdvice.StartGenerateProposal PrepackingAdvice.StartMultiMain PrepackingAdvice.StartOverview PrepackingAdvice.StartPrintPackingSheet
