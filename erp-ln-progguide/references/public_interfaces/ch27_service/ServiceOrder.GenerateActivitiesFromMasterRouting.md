# ServiceOrder.GenerateActivitiesFromMasterRouting

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1413-1414

```baan
DLL:   tsextsocapi
This function is available from     2021.08 (KB2197097  ).
Syntax: long ServiceOrder.GenerateActivitiesFromMasterRouting(
const   domain  tcorno           iServiceOrder fixed,
const           boolean          iUseAttributesFromOrder,
const   domain  tsbsc.clst       iInstallationGroup fixed,
const   domain  tcitem           iItem fixed,
const   domain  tcibd.sern       iSerialNumber fixed,
const   domain  tsacm.cact       iMasterRouting fixed,
const           long             iNumberOfRoutingOptions,
const   domain  tsacm.cact       iRoutingOptions() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : With this function Service Order Activities (tssoc210) for a
certain Service Order (iServiceOrder) can be
generated based on a master routing (iMasterRouting).
With the set of input variables
iUseAttributesFromOrder/iInstallationGroup/iItem
/iSerialNumber there is control what the installation
group, item and serial number on the created service order
activities is going to be.
See the description of these input arguments for more info.
With the set input variables iNumberOfRoutingOptions and
the array iRoutingOptions, the user can control the
list of routing options which has to be executed for the
given master routing. See the description of these input
arguments for more info.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   : iServiceOrder
The service order for which the master routing has
to be executed (mandatory input and should exist).
iUseAttributesFromOrder
If this boolean is set to True, then the activities
(tssoc210) which are going to be created from the given
master routing are using the installation group/item and
serial number from the service order header (tssoc200).
If this boolean is set to False, then the installation
group/item/serial number which are going to be used on
the created service order activities are taken from
the input arguments iInstallationGroup/iItem and
iSerialNumber.
iInstallationGroup
If iUseAttributesFromOrder is set to False,
then the iInstallationGroup is the installation group
which is used on the created service order activities.
If iUseAttributesFromOrder is set to True,
then this input argument is ignored.
iItem
If iUseAttributesFromOrder is set to False,
then the iItem is the item which is used on the created
service order activities.
If iUseAttributesFromOrder is set to True,
then this input argument is ignored.
iSerialNumber
If iUseAttributesFromOrder is set to False,
then the iSerialNumber is the serial number which is
used on the created service order activities.
If iUseAttributesFromOrder is set to True,
then this input argument is ignored.
iMasterRouting
The master routing which is going to be used to
generate the service order activities.
(mandatory input and should exist).
iNumberOfRoutingOptions
If the iNumberOfRoutingOptions is specified as zero,
then, if multiple routing options are present for the
specified master routing, the default routing option is
executed.
If the iNumberOfRoutingOptions is not zero, then
the routing options from the array iRoutingOptions are
executed.
The maximum number of routing options which can be
used is 10.
iRoutingOptions
The array with routing options which need to be
executed for the iMasterRouting. They are only
considered if the iNumberOfRoutingOptions is unequal to
zero. If iNumberOfRoutingOptions is not zero, then the
first iNumberOfRoutingOptions array elements should
exist (allocated) and should not be empty.
Note that if an array is given with routing options
which are not related to the iMasterRouting then
no service order activities will be created, so the
system does not check the validity of these routing
options.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Output  : N.A.
Return  : 0                                           - No error
<> 0                                                  - An error occurred
```
