# ProductAvailability.GetWhenAvailableSchedule

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ProductAvailability
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 581-582

```baan
DLL:   cpextrmpapi
This function is available from 2025.02 (KB3524293).
Syntax: long ProductAvailability.GetWhenAvailableSchedule(
domain  tcplnc           iScenario,
domain  tcitem           iItem,
domain  tcncmp           iCompany,
domain  tcqst1           iQuantity,
domain  tccuni           iQuantityUnit,
long             iProcessingOptionSet,
ref             long             oNumberOfScheduleLines,
ref     domain  tcqsl1           oAvailabilitySchedule(),
ref     domain  tcdate           oWhenAvailableSchedule(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to return the list of quantities
and dates detailing when certain quantities of a given plan item
are planned to be in a given warehouse. Returns the same data as
the When Available form command on session cprrp4800m000.
Pre:    -
Post:   -
Input:  iScenario               - Planning Scenarion. Mandatory.
iItem                   - Item. Mandatory
iCompany                - Ordering Company. Mandatory.
iQuantity               - Ordered Quantity. Mandatory.
iQuantityUnit           - Ordered Quantity Unit. Mandatory.
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "ATP Handling" (cprrp4800m000)and are not explained in
further detail here. Please refer to the session help for additional
information.
Print options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
If the Processing Option "ReportWarnings" is set to "tcyesno.yes" then
all the warning messages that are generated will be stored in the
oExceptionID. oExceptionMessage will have the last generated warning
message and oExceptionID will have all the generated warning messages in
XML structure.
NAME                                    TYPE                    DEFAULT
Channel                         domain  tcmcs.chan      ""
ProductVariant                  domain  tccpva          0
EffectiveUnit                   domain  tcuef.effn      0
Warehouse                       domain  tccwar          ""
DeliveryDate                    domain  tcdate          Current date
OrderType                       domain  tckoor          tckoor.not.appl
OrderNumber                     domain  cporno          ""
OrderTransactionType            domain  tckotr          tckotr.requirement.
OrderLinePositionNumber         domain  tcpono          0
OrderLineSequenceNumber         domain  tcpono          0
LotSize                         domain  tdqsl1          0
CheckFamily                     domain  tcyesno         tcyesno.yes
CheckCapacity                   domain  tcyesno         tcyesno.yes
CheckComponent                  domain  tcyesno         tcyesno.yes
CheckChannel                    domain  tcyesno         tcyesno.yes
ReportWarnings                  domain  tcyesno         tcyesno.no
DemandPeggingType               domain  tcpgtp          tcpgtp.not.appl
SoldToBusinessPartner           domain  tccom.bpid      ""
ShipToBusinessPartner           domain  tccom.bpid      ""
BusinessObjectType              domain  tcalbt          tcalbt.not.appl
BusinessObject                  domain  tcboid          ""
BusinessObjectReference         domain  tcborf          ""
Reference                       domain  tcrefa          ""
UseUnallocatedInventory         domain  tcyesno         tcyesno.yes
ProjectPegProject               domain  tccprj          ""
ProjectPegElement               domain  tccspa          ""
ProjectPegActivity              domain  tccact          ""
Output: oNumberOfScheduleLines  - The number of schedule lines.
oAvailabilitySchedule   - An array of length oNumberOfScheduleLines.
Every entry denotes the quantity of
the Plan Item that becomes available
at the related date from
oWhenAvailableSchedule. Quantities are
not cumulative.
Must be declared based.
oWhenAvailableSchedule  - An array of length oNumberOfScheduleLines.
Every entry denotes the date at which
the related quantity from
oAvailabilitySchedule is available.
Must be declared based.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Otherwise.
```
