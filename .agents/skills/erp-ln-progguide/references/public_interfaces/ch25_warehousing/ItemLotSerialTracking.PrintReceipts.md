# ItemLotSerialTracking.PrintReceipts

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemLotSerialTracking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1134-1135

```baan
DLL:   whextltcapi
This function is available from 2024.04 (KB2328014).
Syntax: long ItemLotSerialTracking.PrintReceipts(
domain  tcitem           iItem,
domain  tcclot           iLotCode,
domain  tcibd.sern       iSerialNumber,
domain  whltc.tord       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This public interface will print the receipt for lots and
serials using the defaults or options as provided in the
iProcessingOptionSet.
Selection range fields (From/To) provided in the
iProcessingOptionSet are ignored when iItem/iLotCode/
/iSerialNumber/iOrderNumber is filled.
In that case the receipts are printed for the given arguments.
Pre:    The report must be opened for the iDevice.
Post:   The report must be closed for the iDevice.
Input:  iItem                   Optional
iLotCode                Optional
iSerialNumber           Optional
iOrderOrigin            Mandatory
iOrderNumber            Optional
iOrderLine              Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Print Receipts for Lots and Serials (whltc3401m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
LotFrom                         domain tcclot           Minimum Value
LotTo                           domain tcclot           Maximum Value
SerialFrom                      domain tcibd.sern       Minimum Value
SerialTo                        domain tcibd.sern       Maximum Value
OrderOrigin                     domain whltc.tord       whltc.tord.purchase
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
StartSearch                     domain whltc.selo       whltc.selo.serial
PrintType                       domain whltc.klot       whltc.klot.all
TrackBoth                       domain tcyesno          tcyesno.no
NewPage                         domain tcyesno          tcyesno.no
PrintLevel                      domain whltc.levl       whltc.levl.first
PrintTill                       domain tcdate           current date
Output: o.data.processed        - true:  Receipts Printed.
false: Nothing Printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK
<> 0                    - Error.
```
