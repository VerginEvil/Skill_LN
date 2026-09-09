# Pricing.StartPriceSimulator

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 520-525

```baan
DLL:   tdextpcgapi
This function is available from 2024.04 (KB2328014).
Syntax: long Pricing.StartPriceSimulator(
long             iStartMode,
domain  tdpcg.tyor       iTypeOfOrder,
domain  tccom.bpid       iBusinessPartner,
domain  tcitem           iGenericItem,
domain  tccitt           iItemCodeSystem,
domain  tcaitm           iItemCodeSystemItem mb,
domain  tcitem           iItem,
domain  tcmpnr           iManufacturerPartNumber,
domain  tcmcs.cmnf       iManufacturer,
domain  tcuef.effn       iEffectivityUnit,
domain  tdpcg.prit       iPriceType,
domain  tcccur           iCurrency,
domain  tcqsl1           iQuantity,
domain  tccuni           iQuantityUnit,
domain  tcdate           iPriceDate,
domain  tcsite           iSite,
domain  tccwar           iWarehouse,
domain  tcyesno          iShowItemBpSignals,
domain  tcyesno          iInternalRepairPriceBook,
domain  tcyesno          iIncludeFreightCosts,
domain  tccom.infr       iInvoiceFreightCostBasedOn,
domain  tcyesno          iIncludeATP,
domain  tcatpc           iATPHandling,
domain  tdsls.corg       iSalesOrderOrigin,
domain  tcmcs.chan       iSalesBusinessPartnerChannel,
domain  tccom.bpid       iPurchaseShipFromBusinessPartner,
domain  tdpur.corg       iPurchaseOrderOrigin,
domain  tcsite           iPurchaseSubcontractorSite,
domain  tcmcs.cmnf       iPurchaseManufacturer,
domain  tccwoc           iServiceOffice,
domain  tccotp           iServiceType,
domain  tccitg           iServiceItemGroup,
domain  tccitg           iServiceSerializedItemGroup,
domain  tcitem           iServiceMaintainedItem,
domain  tcibd.sern       iServiceMaintainedSerialNumber,
domain  tcclst           iServiceInstallationGroup,
domain  tccreg           iServiceArea,
domain  tcacm.cact       iServiceReferenceActivity,
domain  tcacm.cact       iServiceMasterRouting,
domain  tcacm.cact       iServiceRoutingOption,
domain  tcmcs.cmnf       iServiceManufacturer,
domain  tdpcg.frcl       iFreightClass,
domain  tdpcg.rbno       iFreightRateBasisNumber,
domain  tccwoc           iFreightShippingOffice,
domain  tccpay           iFreightPaymentTerms,
domain  tccom.bpid       iPricingBusinessPartner,
domain  tccplt           iPriceList,
domain  tcpaym           iPaymentMethod,
domain  tccdec           iDeliveryTerms,
domain  tccreg           iArea,
domain  tccotp           iOrderType,
domain  tccwoc           iOffice,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tdpcg.pror       iPriceOrigin,
domain  tccom.bpid       iInvoiceFromBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Price Simulator
(tdpcg0200m300).
Input:  iStartMode                      - Not Used
|***************************************************************
|* Mandatory input arguments
|*
|* These input arguments are mandatory to be filled.
|***************************************************************
iTypeOfOrder                    - Type of Order. Controls many
other input arguments. For
example, when Type of Order
is 'General Sales', arguments
that are particular Purchase
Attributes or Service
Attributes are not allowed
to be filled.
(General Attribute)
iPriceType                      - Price Type
(General Attribute)
iShowItemBpSignals              - Show Item / Business Partner Signals
(General Attribute)
iInternalRepairPriceBook        - Use Internal Repair Price Book
(Service Attribute)
iIncludeFreightCosts            - Include freight Costs
(Freight Attribute)
iInvoiceFreightCostBasedOn      - Invoice Freight Cost Based On
(Freight Attribute)
iIncludeATP                     - Include ATP
(General Attribute)
iATPHandling                    - ATP
(General Attribute)
iItem                           - Item
(General Attribute)
iCurrency                       - Currency
(General Attribute)
|***************************************************************
|* Checked input arguments
|*
|* These input arguments, being empty or being (correctly)
|* filled, are validated based on other input arguments like
|* for instance the iTypeOfOrder input argument.
|***************************************************************
iGenericItem                    - Generic Item
(General Attribute)
iItemCodeSystemItem             - Item Code System Item
(General Attribute)
iManufacturerPartNumbe          - Manufacturer Part Number
(General Attribute)
iManufacturer                   - Manufacturer
(General Attribute)
iEffectivityUnit                - Effectivity Unit
(General Attribute)
iSite                           - Site
(General Attribute)
iSalesOrderOrigin               - Order Origin
(Sales Attribute)
iSalesBusinessPartnerChannel    - Business Partner Channel
(Sales Attribute)
iPurchaseShipFromBusinessPartner- Schip-from Business
Partner
(Purchase Attribute)
iPurchaseOrderOrigin            - Order Origin
(Purchase Attribute)
iPurchaseSubcontractorSite      - Subcontractor Site
(Purchase Attribute)
iPurchaseManufacturer           - Manufacturer
(Purchase Attribute)
iServiceOffice                  - Service Office
(Service Attribute)
iServiceType                    - Service Type
(Service Attribute)
iServiceItemGroup               - Item Group
(Service Attribute)
iServiceSerializedItemGroup     - Serialized Item Group
(Service Attribute)
iServiceMaintainedItem          - Item
(Service Attribute)
iServiceMaintainedSerialNumber  - Serial Number
(Service Attribute)
iServiceInstallationGroup       - Installation Group
(Service Attribute)
iServiceArea                    - Service Area
(Service Attribute)
iServiceReferenceActivity       - Reference Activity
(Service Attribute)
iServiceMasterRouting           - Master Routing
(Service Attribute)
iServiceRoutingOption           - Routing Option
(Service Attribute)
iServiceManufacturer            - Manufacturer
(Service Attribute)
iFreightClass                   - Freight Class
(Freight Attribute)
iFreightRateBasisNumber         - Rate Basis Number
(Freight Attribute)
iFreightShippingOffice          - Shipping Office
(Freight Attribute)
iFreightPaymentTerms            - Payment Terms
(Freight Attribute)
iOrderType                      - Order Type
(Sales/Purchase Attribute)
iOffice                         - Office
(Sales/Purchase Attribute)
iShipToBusinessPartner          - Ship-to Business Partner
(Sales/Service Attribute)
iInvoiceToBusinessPartner       - Invoice-to Business Partner
(Sales/Service Attribute)
iPriceOrigin                    - Price Origin
(Sales/Service Attribute)
iInvoiceFromBusinessPartner     - Invoice-from Business Partner
(Purchase/Service Attribute)
|***************************************************************
|* Free input arguments
|*
|* These input arguments are allowed to be empty or filled.
|***************************************************************
iBusinessPartner                - Business Partner
(General Attribute)
iItemCodeSystem                 - Item Code System
(General Attribute)
iQuantity                       - Quantity
(General Attribute)
iQuantityUnit                   - Quantity Unit
(General Attribute)
iPriceDate                      - Price Date
(General Attribute)
iWarehouse                      - Warehouse
(General Attribute)
iPricingBusinessPartner         - Pricing Business Partner
(Sales/Purchase/Service Attribute)
iPriceList                      - Price List
(Sales/Purchase/Service Attribute)
iPaymentMethod                  - Payment Method
(Sales/Purchase/Service Attribute)
iDeliveryTerms                  - Delivery Terms
(Sales/Purchase/Service Attribute)
iArea                           - Area
(Sales/Purchase/Service Attribute)
Output: oExceptionMessage               - The last message if any
message is found. If more than
one message is given, these
are present in the
oExceptionID.
oExceptionID                    - An ID that refers to the
exception information. Use
the functions in Exception to
get all relevant information.
Return: 0                               - Session started
<> 0                            - Error.
```
