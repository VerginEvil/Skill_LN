# Item.GetSupplier

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 181-182

```baan
DLL:   tdextipuapi
Syntax: long Item.GetSupplier(
domain  tcncmp           iLogisticCompany,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tcefex.date      iEffectiveDate,
domain  tcqrd2           iQuantity,
boolean          iForceRead,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tccom.bpid       oShipFromBusinessPartner,
ref             boolean          oBusinessPartnerFoundOnItemBPLevel,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns the first valid Buy-from Business Partner
and Ship                      -from Business Partner based on priority for the
specified Item/Item Group.
Notes:
-                       In this context, Item - Purchase BP level refers to
Item                         - Purchase BP or Item - Purchase BP by Site.
Item                         - Purchase level refers to Item - Purchase or Item -
Purchase by Site.
-                       Search is performed in Item - Purchase BP tables and Item -
Purchase tables.
-                       If i.site is filled, then the search will first be performed
in Item                         - Purchase (BP) by Site tables. If no entry is found
there, then Item                         - Purchase (BP) tables are searched.
-                       Only active BPs will be returned.
Selecting data to retrieve BPs is done in the following order:
1) Item                      -level: Item - Purchase if approved on Item - Purchase BP
level.
2) Item                      -level: Item - Purchase BP, approved single source BP.
3) Item                      -level: Item - Purchase BP, approved BP.
4) Item                      -group-level: Item - Purchase if approved on Item -
Purchase BP level.
5) Item                      -group-level: Item - Purchase BP, approved single source
BP.
6) Item                      -group-level: Item - Purchase BP, approved BP.
If Sourcing from Approved Vendors is not checked on Item                       -
Purchase:
7) Item                      -level: Item - Purchase.
Pre:    NA
Post:   NA
Input:  iLogisticCompany                      - Logistic Company: Mandatory
iItemGroup                                    - Item Group; Optional if Item is
filled.
iItem                                         - Item; Mandatory if Item Group not
filled.
iSite                                         - Site: Not Mandatory
iEffectiveDate                                - Mandatory; use utc.num() if current
date is needed.
iQuantity                                     - Optional; use 0.0 if no minimum order
quantity must be considered.
iForceRead                                    - Option to force new query in stead of
using cached information
Output: oBuyFromBusinessPartner               - Buy-from Business Partner
oShipFromBusinessPartner                      - Ship-from Business Partner
oBusinessPartnerFoundOnItemBPLevel                            -
True: Found on Item BP level.
False: No BP found or not found on
Item                                                 - BP level.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Data read
<> 0                                          - An error occurred
```
