# WorkOrder.GenerateActivitiesFromMasterRouting

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1491-1492

```baan
DLL:   tsextwcsapi
This function is available from     2021.11 (KB2211358  ).
Syntax: long WorkOrder.GenerateActivitiesFromMasterRouting(
const   domain  tcorno           iWorkOrder fixed,
const   domain  tsacm.cact       iMasterRouting fixed,
const           long             iNumberOfRoutingOptions,
const   domain  tsacm.cact       iRoutingOptions() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : With this function work order activities (tswcs210) for a
certain work order (iWorkOrder) can be
generated based on a master routing (iMasterRouting).
With the set input variables iNumberOfRoutingOptions and
the array iRoutingOptions, the user can control the
list of routing options which has to be executed for the
given master routing. See the description of these input
arguments for more info.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   : iWorkOrder
The work order for which the master routing has
to be executed (mandatory input and should exist).
iMasterRouting
The master routing which is going to be used to
generate the service order activities.
(mandatory input and should exist).
iNumberOfRoutingOptions
If the iNumberOfRoutingOptions is specified as zero,
then, if multiple routing options are present for the
specified master routing, the default routing option is
executed. If in this scenario the default routing option
has not been specified, then an error is returned.
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
no work order activities will be created, so the
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
