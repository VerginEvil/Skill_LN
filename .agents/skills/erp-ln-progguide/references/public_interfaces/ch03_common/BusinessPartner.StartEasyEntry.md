# BusinessPartner.StartEasyEntry

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 130-132

```baan
DLL:   tcextcomapi
This function is available from 2021.05 (KB2188824).
Syntax: long BusinessPartner.StartEasyEntry(
long             iStartMode,
domain  tccom.bpid       iBusinessPartnerSerie,
domain  tcbpid.nama      iBusinessPartnerName mb,
domain  tcsern           iBusinessPartnerDefaults,
domain  tcbprl           iBusinessPartnerRole,
domain  tcyesno          iCreateSoldToRole,
domain  tcyesno          iCreateBuyFromRole,
domain  tcyesno          iCreateShipToRole,
domain  tcyesno          iCreateShipFromRole,
domain  tcyesno          iCreateInvoiceToRole,
domain  tcyesno          iCreateInvoiceFromRole,
domain  tcyesno          iCreatePayByRole,
domain  tcyesno          iCreatePayToRole,
domain  tccom.cadr       iAddressCode,
domain  tccadr.nama      iAddressName mb,
domain  tcccty           iCountry,
domain  tcpstc           iZipCode mb,
domain  tcmcs.cste       iStateProvince,
domain  tcnama           iCounty mb,
domain  tccity           iCity,
domain  tccadr.namc      iStreet mb,
domain  tccom.nmbr       iHouseNumber mb,
domain  tctax.txnb       iTaxNumber,
domain  tccom.ccnt       iContact,
domain  tcmcs.st80m      iContactName mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Easy Entry Business
Partners - (tccom4201m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible value is:
MODAL   -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.      (mandatory)
iBusinessPartnerSerie   - Business Partner Serie        (mandatory)
iBusinessPartnerName    - Business Partner Name         (mandatory)
iBusinessPartnerDefaults- Business Partner Defaults     (mandatory)
iBusinessPartnerRole    - Business Partner Role
Note: The session Easy Entry Business Partners wil not
always use all iCreate<**>Role input field.
This depends on the company type
eg: In a logistic company the financial roles will not
be created
iCreateSoldToRole       - Create Sold To Role
(customer/logistic)
iCreateBuyFromRole      - Create Buy From Role
(supplier/logistic)
iCreateShipToRole       - Create Ship To Role
(customer/logistic)
iCreateShipFromRole     - Create Ship From Role
(supplier/logistic)
iCreateInvoiceToRole    - Create Invoice To Role
(customer/financial)
iCreateInvoiceFromRole  - Create Invoice From Role
(supplier/financial)
iCreatePayByRole        - Create Pay By Role
(customer/financial)
iCreatePayToRole        - Create Pay To Role
(supplier/financial)
iAddressCode            - Address Code or address series
Note: if iAddressCode is an existing address
instead of a series code, the values of
the address related input fields are ignored.
iAddressName            - Address Name
iCountry                - Country
iZipCode                - Zip Code/ Postal code
iStateProvince          - State or Province
iCounty                 - County
iCity                   - City
iStreet                 - Street
iHouseNumber            - House number
iTaxNumber              - Tax Number
iContact                - Contact or contact serie
Note: if iContact is an existing Contact
instead of a series code, the value of
the iContactName is ignored.
iContactName            - Full Contact Name
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
