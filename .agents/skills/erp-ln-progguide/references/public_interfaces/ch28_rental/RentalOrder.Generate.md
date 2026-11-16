# RentalOrder.Generate

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1563-1567

```baan
DLL:   tsextsocapi
This function is available from 2024.05 (KB2331668).
Syntax: long RentalOrder.Generate(
long             iProcessingOptionSet,
ref     domain  tcorno           oRentalOrder,
ref     domain  tsmdm.acln       oAgreementLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to:
- Generate a new Rental Order.
- Add a Rental Agreement Line to an existing Order.
- Process a rental request or rental request line.
Rental Order can be generated based on the given Equipment,
Rental Template or a combination of these.
If a template list is passed, for each of the templates an
agreement is created.
If a rental request and the request line are passed, for this
specific line an agreement is created. The line is set to
Processed.
If a request is passed without a line, all lines are processed
and the request is set to Processed.
Before calling RentalOrder.Generate(), call
ProcessingOptionSet.Create(). After the call the option set
can be deleted by calling ProcessingOptionSet.Delete()
Pre:    db.retry.point() set;
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   commit/abort transaction;
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iProcessingOptionSet: Mandatory
Processing Options which are set while the required Implemented
Software Component is not available are ignored.
NAME                    TYPE                    DEFAULT
================================================================
RentalOrder
domain  tcorno          empty
Existing rental order to which the line(s) to be created
must be added.
AgreementLine
domain  tsmdm.acln      zero
The Rental Agreement Line to which an equipment
line will be added. For this the argument Equipment
must hold an item of type Rental Product.
OrderSeries
domain  tcseri          empty
The order series used when generating new rental order.
If left empty the default series defined on the rental
office or user profile will be used.
RentalOffice
domain  tccwoc          empty
The rental office to be used on the rental order to be
created.
ServiceType
domain  tsmdm.cstp      empty
The service type of type Rental to be used on the
created Rental Order or Agreement.
RentedToBusinessPartner
domain  tccom.bpid      empty
The Rented-to Business Partner to be used on the to be
created Rental Order.
LocationAddress
domain  tccom.cadr      empty
The location address where the equipment will be
located when it is rented out. This address will be
stored on the Rental Agreement to be created.
EquipmentProjectSegment
domain  tccprj          empty
EquipmentItemSegment
domain  tcitem          empty
The item that will be rented out in two segments which
will be combined.
The item type can be Equipment or Rental Product.
When the item is serialized, the item and serial number
will be passed to the rental agreements item and
serial number, respectively.
If the item is anonymous for both item types, an
equipment line with delivery type From Rental Fleet
will be created.
SerialNumber
domain  tcibd.sern      empty
The serial number of the equipment rented out. For
these item In service serialized items the check box
Rentable must be selected.
RentalTemplate
domain  tsacm.cact      empty
The rental template used on the to be generated rental
agreement. The rental template is used to define a
default set of cost line for rental.
The rental template and rental template list cannot
be used both at the same time.
NumberOfUnits
domain  tcnoun          1
The number of units of the rental templates used on
the to be generated rental agreement.
RentalTemplateList
domain  tsacm.cact      empty
A list of rental templates. For each rental template an
agreement line will be created.
PlannedOnHireTime
domain  tcdate          0
The date the rental is expected to start.
PlannedOffHireTime
domain  tcdate          0
The date the rental is expected to end.
RentalPeriod
domain  tcdays          0
The rental period expressed in the period unit.
RentalPeriodUnit
domain  tctmun          tctmun.days
The rental period unit with possible values:
- Hours
- Days
- Weeks
- Months
- Years
ExpectedReturnTime
domain  tcdays          0
The date the rented out equipment is expected to be
returned.
Project
domain  tccprj          empty
The project to which the generated Rental Order or
Agreement is linked.
ProjectElement
domain  tccspa          empty
The Element to which the generated Rental Order or
Agreement is linked.
ProjectActivity
domain  tccact          empty
The Activity to which the generated Rental Order or
Agreement is linked.
ExternalHire
domain  tcyesno         tcyesno.no
Indicates that the rented out equipment is externally
hired.
Supplier
domain  tccom.bpid      empty
The Business Partner who supplies the externally hired
equipment.
HireRate
domain  tcpric          0
The external hire cost rate expressed in the hire
currency and unit.
HireCurrency
domain  tcccur          empty
The external hire currency.
HireUnit
domain  tccuni          empty
The external hire unit.
ExternalSerial
domain  tcibd.sern      empty
The serial number of the externally to be hired
equipment.
RentalRequest
domain  tcorno          empty
The rental request which is being processed.
RentalRequestLine
domain  tcpono          0
The rental request line which is being processed.
RentalRequestLineQuantity
domain  tsmdm.qmat      0
The rental request line quantity expressed in the
request line unit.
RentalRequestLineQuantityUnit
domain  tccuni          empty
The rental request line quantity unit.
BillingSchedule
domain  tsmdm.bsch      empty
Schedule used on the agreement. Schedule defines the
periods for which the usage must be registered and
invoiced.
AutomaticBilling
domain  tcyesno         tcyesno.no
If selected and a billing schedule is used the
registration and billing of the usage will be done
automatically (by batch jobs).
Output: o.rental.order
The existing or created rental order.
o.agreement line
The created agreement line, or the first agreement line
in case multiple are created.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No Error
<> 0    - Error
```
