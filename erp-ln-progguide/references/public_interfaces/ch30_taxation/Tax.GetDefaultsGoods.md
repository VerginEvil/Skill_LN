# Tax.GetDefaultsGoods

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1622-1625

```baan
DLL:   tcexttaxapi
This function is available from     2025.06 (KB3525116  ).
Syntax: long Tax.GetDefaultsGoods(
domain  tcncmp           iFinancialCompany,
const   domain  tccom.bpid       iShipFromBusinessPartner,
const   domain  tccom.bpid       iShipToBusinessPartner,
const   domain  tccom.bpid       iInvoiceFromBusinessPartner,
const   domain  tccom.bpid       iInvoiceToBusinessPartner,
const   domain  tccom.bpid       iBuyFromBusinessPartner,
const   domain  tccom.bpid       iSoldToBusinessPartner,
domain  tctax.oorg       iOriginalTaxOrigin,
domain  tctax.oorg       iCurrentTaxOrigin,
domain  tcitr.scen       iIntercompanyTradeScenario,
domain  tccls.scen       iClassificationScenario,
const   domain  tcitem           iItem,
domain  tckitm           iItemType,
const   domain  tccitg           iItemGroup,
const   domain  tcatse           iAttributeSet,
const   domain  tcgeoc           iGeoDestination,
const   domain  tcgeoc           iGeoOrigin,
const   domain  tcgeoc           iGeoPostalAddress,
const   domain  tcsite           iShipFromSite,
const   domain  tcsite           iShipToSite,
const   domain  tccom.cadr       iShipFromAddress,
const   domain  tccom.cadr       iShipToAddress,
const   domain  tccom.cadr       iBuyFromAddress,
const   domain  tccom.cadr       iSoldToAddress,
const   domain  tccom.cadr       iInvoiceFromAddress,
const   domain  tccom.cadr       iInvoiceToAddress,
domain  tcncmp           iOperationalCompany,
const   domain  tccdec           iTermsOfDelivery,
const   domain  tcptpa           iPointOfTitlePassage,
domain  tctax.ttyp       iTradeType,
domain  tcdate           iDateUTC,
domain  tctax.vtbo       iVatBasedOn,
const   domain  tccwar           iWarehouse,
const   domain  tccwoc           iWorkCenter,
const   domain  tcccty           iPurchaseTaxCountry,
const   domain  tccvat           iPurchaseTaxCode,
const   domain  tccwoc           iAdminDepartment,
const   domain  tccwoc           iFinancialDepartment,
const   domain  tccom.cadr       iFinancialDepartmentAddress,
const   domain  tctax.bpcl       iTaxClassification,
const   domain  tccsec           iBusinessSector,
const   domain  tcccat           iCategory,
const   domain  tccspa           iElement,
const   domain  tccact           iActivity,
domain  tcmcs.cotp       iCostType,
const   domain  tcmcs.coob       iCostObject,
domain  tcyesno          iTaxApplicable,
ref     domain  tcccty           oTaxCountry,
ref     domain  tcmcs.cste       oTaxState,
ref     domain  tcezty           oTaxEconomicZoneType,
ref     domain  tccvat           oTaxCode,
ref     domain  tcccty           oBusinessPartnerTaxCountry,
ref     domain  tcmcs.cste       oBusinessPartnerTaxState,
ref     domain  tcezty           oBusinessPartnerTaxEconomicZoneType,
ref     domain  tcyesno          oExempt,
ref     domain  tcfovn           oExemptCertificate,
ref     domain  tccdis           oExemptReason,
ref     domain  tcmcs.s250m      oOverallMessage mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to get the default tax related information
based on the given input.
This function determines the appropriate
* Tax Country
* Tax State
* Tax Economic Zone Type
* Tax Code
* Business Partner Tax Country
* Business Partner Tax State
* Business Partner Tax Economic Zone Type
* Exempt
* Exempt Certificate
* Exempt Reason
to be used when calling from application.
* The Tax Country is the Country where you as Company are
responsible for Tax.
* The Tax Code is the percentage on which the Tax amount is
based on.
* the Business Partner Tax Country is the Country where the
Business Partner is responsible for Tax.
Pre:    All arguments should be filled whenever possible.
Because input arguments are valid for both Sales and Purchase
transactions, not all arguments can be filled in all cases.
Post:   NotApplicable
Input:  iFinancialCompany                             - Financial Company
iShipFromBusinessPartner                              - Ship-from Business Partner
iShipToBusinessPartner                                - Ship-to Business Partner
iInvoiceFromBusinessPartner                           - Invoice-from Business Partner
iInvoiceToBusinessPartner                             - Invoice-to Business Partner
iBuyFromBusinessPartner                               - Buy-from Business Partner
iSoldToBusinessPartner                                - Sold-to Business Partner
iOriginalTaxOrigin                                    - Original Tax Origin
iCurrentTaxOrigin                                     - Current Tax Origin
iIntercompanyTradeScenario                            - Intercompany Trade Order
Scenario
iClassificationScenario                               - Classification Scenario
iItem                                                 - Item
iItemType                                             - Item Type
iItemGroup                                            - Item Group
iAttributeSet                                         - Arrtibute Set
iGeoDestination                                       - GEO Code Destination
Hierarchy necessary to determine GEO codes:
Modules: Sales
a. Use pstc.dl if non                                         -blank
b. If pstc.dl is blank, then use pstc.cs
if non                                            -blank.
c. If pstc.cs is blank, then use the
address of ship                                            -to business partner
Modules: Purchase
a. Use pstc.dl if non                                         -blank
b. If pstc.dl is blank, then use pstc.wh
if non                                            -blank.
c. If pstc.wh is non                                         -blank, then use the
address of the company associated on
order.
iGeoOrigin                                            - GEO Code Origin
Hierarchy necessary to determine GEO codes:
Modules: Sales
a. Use pstc.wh if non                                         -blank
b. If pstc.wh is blank, then use the
address of the company associated on
the order.
Modules: Purchase
a. Use pstc.cs if non                                         -blank
b. If pstc.cs is blank, then the address
of the ship                                            -from business partner.
iGeoPostalAddress                                     - GEO Code Postal Address
Hierarchy necessary to determine GEO codes:
Modules: Sales
Modules: Purchase
a. Use pstc.pa
iShipFromSite                                         - Ship-from Site
iShipToSite                                           - Ship-to Site
iShipFromAddress                                      - Ship-from Address
iShipToAddress                                        - Ship-to Address
iBuyFromAddress                                       - Buy-from Address
iSoldToAddress                                        - Sold-to Address
iInvoiceFromAddress                                   - Invoice-from Address
iInvoiceToAddress                                     - Invoice-to Address
iOperationalCompany                                   - Operational Company
iTermsOfDelivery                                      - Terms of Delivery
iPointOfTitlePassage                      - Point of Title Passage
iTradeType                                            - Trade Type
* tctax.ttyp.dir.del (when called from tdpur)
* tctax.ttyp.dir.del.int.inv (when called from whinh)
* tctax.ttyp.triangular (when called from whinh)
* tctax.ttyp.bilateral (when called from whinh)
* tctax.ttyp.not.appl (in all other cases)
iDateUTC                                              - UTC Date
iVatBasedOn                                           - VAT Based on
iWarehouse                                            - Warehouse
iWorkCenter                                           - Work Center
iPurchaseTaxCountry                                   - Purchase Tax Country
iPurchaseTaxCode                                      - Purchase Tax Code
iAdminDepartment                                      - Admin Department
iFinancialDepartment                                  - Financial Department
iFinancialDepartmentAddress                           - Financial Department Address
iTaxClassification                                    - Tax Classification
iBusinessSector                                       - Business Sector
iCategory                                             - Category
iElement                                              - Element
iActivity                                             - Activity
iCostType                                             - Cost Type
iCostObject                                           - Cost Object
iTaxApplicable                                        - Tax Applicable
No:                                           - In case tdsls000.atin.4 (Apply Tax to
Installments) = 'No' and the
transaction is an installment.
-                                               In case of advance payment requests
from Contract
Yes:                                          - In all other cases.
Output: oTaxCountry                                   - Tax Country
oTaxState                                             - Tax State
oTaxEconomicZoneType                                  - Tax Economic Zone Type
oTaxCode                                              - Tax Code
oBusinessPartnerTaxCountry                            - Business Partner Tax Country
oBusinessPartnerTaxState                              - Business Partner Tax State
oBusinessPartnerTaxEconomicZoneType
-                                                       Business Partner Economic Zone
Type
oExempt                                               - Exempt
oExemptCertificate                                    - Exempt Certificate
oExemptReason                                         - Exempt Reason
oOverallMessage                                       - Overall Message
Return: 0/DALHOOKERROR
```
