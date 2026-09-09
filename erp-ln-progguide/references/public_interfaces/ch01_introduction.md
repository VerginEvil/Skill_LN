# Introduction

> Chapter: Chapter 1 Introduction
>
> Group: -
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 71-86

## About this guide

## Intended audience

This guide is intended for IT professionals working in implementation projects or IT optimization phases for Infor LN. Basic knowledge about the Infor LN software structure and Infor LN’s 4GL programming language is a pre-requisite.

## Related documents

You can find these documents on docs.infor.com:
• Infor LN Studio Application Development Guide
• Infor LN Studio Integration Development Guide
• Infor LN Extensions Development Guide
You can find the Infor ES Programmer's Guide in KB2924522. The content of this guide is also available in the help pages of Infor LN Studio.

## Contacting Infor

If you have questions about Infor products, go to Infor Concierge at https://concierge.infor.com and create a support incident.
For the latest documentation, go to Documentation Central at docs.infor.com. We recommend that you check this website periodically for updated documentation.

## Chapter 1 Introduction

Infor LN is a standard ERP application with rich functionality. With its built-in flexibility with parameters, workflows, dynamic processes, it can be adjusted to serve the business processes in the industries Infor LN is designed for. To close the small gaps between the standard functionality and the specific business needs, Infor LN offers a variety of extensibility possibilities. The main goal of extensibility is to develop the last-mile functionality for your organization without changing the core standard software components and using only the public interfaces of the standard application. In this way, you can develop the extensions fully separated from the standard components and upgrading the standard software will therefore not result in additional efforts and costs for upgrading the customizations. Extensions are not influenced by the upgrade process.

## Public Interfaces

Public Interfaces are methods with LN application functionality that can be called from extensions.
Public Interfaces explained
The development of extensions can be made easier if methods from the LN Application can be used. This can be done by using the so-called LN Public Interfaces. LN Public Interfaces are functions in the LN Application that are available for anyone who develops extensions on LN. The available LN Public Interfaces are visible in LN Studio and in the Extension Modeler. LN Public Interfaces are generic functions with a certain level of complexity that will likely be used by multiple customers. Simple read actions, for example, needs to be developed by customers or implementation partners themselves. Moreover, LN Public Interfaces will perform something what cannot easily be achieved with one or more standard sessions or processes in LN.
How to request a new Public Interface
Apply the following process if you need a new LN Public Interface:
1   Evaluate if the new LN Public Interface is generic and contains a certain level of complexity. Make sure the required feature cannot be achieved with personalizing a standard session or process.
2   Create an incident and clearly describe the required LN Public Interface. Use the Excel Sheet “Request Template for LN Public Interfaces & Process Extensions)” which is attached to KB2003722 in the Infor Customer Portal.
3   Infor Support will create a defect for this incident.
4   Infor Development will review the requested LN Public Interface and will either develop the new LN Public Interface or reject the request. If the LN Public Interface is developed it will be released via the regular delivery process.
5   After the new solution has been installed the customer can use the new LN Public Interface in the extension modeler and/or in LN Studio.
6   Infor Support will complete the incident.
Public Interface example
Find below an example of one of the LN Public Interfaces. This Public Interface converts an amount to another currency.
```baan
long Common.ConvertAmount(
domain    tcncmp        iFinancialCompany,
domain    tcamnt        iSourceAmount,
domain    tcccur        iSourceCurrency,
domain    tcrtyp        iExchangeRateType,
domain    tcdate        iRateDateUTC,
domain    tcccur        iTargetCurrency,
ref    domain    tcamnt        oTargetAmount,
ref    domain    tcmcs.s999m   oExceptionMessage mb,
ref              long          oExceptionID)
```

It is very important to use LN Public Interfaces properly and to catch the errors. For this reason, each Public Interface has the output arguments 'oExceptionMessage' and 'oExceptionID'.
If the Public Interface returns a value unequal to zero, then argument oExceptionMessage is filled for sure with the latest exception message and argument oExceptionID is a reference to an XML-object that contains some more information about the exception. This extra information can be retrieved by using the Public Interface 'Exception' in otcextextapi. It is also important to free up memory by calling Public Interface Exception.Delete(...).
If the Public Interface returns zero, arguments oExceptionMessage and oExceptionID could be filled due to information messages. So, in fact only the return value indicates if a public interface is successful or not.
The next example shows how to implement error handling when using LN Public Interfaces, in this case Common.ConvertAmount to convert an amount to another currency.
#pragma used dll "otcextextapi" #pragma used dll "otcextemmapi" long          exception.id, i domain   tcmcs.s999m   exception.message if Common.ConvertAmount(..., exception.message, exception.id) <> 0 then |* Exception(s) found. for i = 1 to Exception.NumberOfMessages(exception.id) dal.set.error.message("@"& Exception.GetMessage(i)) endfor Exception.Delete(exception.id) return(DALHOOKERROR) else |* Call was successful. Exception messages could exist! Exception.Delete(exception.id) endif To be able to use the Public Interface in your extensions, you need to add a “#pragma used dll” statement for the DLL that contains the Public Interface. The DLL names can be found in the documentation of the available Public Interfaces. Note that the DLL name needs to be preceded by an “o” in the #pragma-statement.
Available Public Interfaces
The next chapters of this document describe the available Public Interfaces for Infor LN (Cloud Edition) and what their usage is.
If the Public Interfaces described in this document are not shown in the Extension Modeler or Infor LN Studio in your environment, it may be necessary to apply a Knowledge Base article (KB) that can be found in the Infor Customer Portal. The applicable KB number is mentioned in the Public Interface description. Appendix A contains an overview of all Public Interfaces per Infor LN Cloud release.
Public Interface to call BDE methods
BDEs (Business Data Entities) are components in Infor LN that are the base for Infor LN’s web services. A special Public Interface is available to call the BDE methods within extensions: BDE.ExecuteMethod. Note that this will not be a real (SOAP) web service call, but the BDE method will be executed internally in LN.
The available BDEs are shown in session “Business Objects” (ttadv7500m000). The BDEs that are available to be called as Public Interface must satisfy the following conditions:
•   The name must not end with “BOD”
•   The Type of Business Object must be ‘Public’
•   The Maintained in Studio checkbox must be checked
•   The action Download WSDL must be available for the BDE.
Proxy DLL
BDE methods are functions that have an XML document as input (the request), and the output is either a response XML document (in case the method succeeded) or a result XML document (in case the method failed). To build the request or to retrieve data from the response or result, you need to use a Proxy DLL that is generated based on the WSDL (Web Service Description Language). To be able to generate a proxy DLL you need to have a Development license (product ID 10146).
Perform the following steps to generate a Proxy DLL:
1   Select the BDE you want to call in your extension in session “Business Objects” (ttadv7500m000).
2   Click Actions>Download WSDL.
3   Save the WSDL in a folder on your PC.
4   Start Infor LN Studio. At least version 10.7.0.389 is needed. For more information about Infor LN Studio see the Related Documents section of this document.
5   If you don’t have an Activity yet, create a new one.
6   Create a new software component of type Library. Enter a name and a description and click Finish.
7   A new library is created, and the editor is opened for it. Check out the library.
8   Right-click in the editor and select Generate Source from WSDL.
9   The “Generate Library from WSDL file” displays. Browse to the WSDL file you saved on your PC in step 3.
10 Click OK.
11 The source is generated. Click Save button.
12 If you need to use the proxy DLL in another LN Studio Activity or another Extensibility Activity, the proxy DLL must be committed by (partially) ending the current Activity.
Coding example
This program creates and releases a Service Order using the Create and ReleaseOrder methods of the ServiceOrder_v4 BDE. The numbers behind |# refer to remarks after the example program.
```baan
#pragma used dll "otcextextapi"                                             |# 1
#pragma used dll "otcextbdeapi"                                             |# 2
```

```baan
function create.and.release.service.order()
{
long    request, response, result
long    so.order, so.act, so.ass
long    ro
long    da
long    ret
long    exceptionid
string  exceptionmessage(1000) mb
domain  tcorno  service.order
db.retry.point()                                                            |# 3
request = Create_CreateRequest.New()                                        |# 4
so.order = Create_ServiceOrder_v4.New("JJD")                                |# 5
Create_ServiceOrder_v4.SetserviceCenter(so.order, "100")                    |# 6
da = Create_DataArea.New()                                                  |# 7
ret = Create_DataArea.AddServiceOrder_v4(da, so.order)
Create_CreateRequest.SetDataArea(request, da)
so.act = Create_ServiceOrderActivity.New()                                  |# 8
ret = Create_ServiceOrder_v4.AddServiceOrderActivity(so.order, so.act)      |# 9
|# 6
Create_ServiceOrderActivity.SetserviceOrderActivityPlannedStartTime(so.act, utc.num())
Create_ServiceOrderActivity.SetserviceOrderActivityPlannedFinishTime(
so.act, utc.num() + 3600)
so.ass = Create_ActivityEngineer.New()                                      |# 10
ret = Create_ServiceOrderActivity.AddActivityEngineer(so.act, so.ass)       |# 11
Create_ActivityEngineer.SetassignmentEngineer(so.ass, "0099101")            |# 6
ret = BDE.ExecuteMethod("ServiceOrder_v4",                                  |# 12
"Create",
request,
response,
result,
exceptionmessage,
exceptionid)
if ret <> 0 then                                                            |# 13
abort.transaction()
message(exceptionmessage)
Exception.Delete(exceptionid)
return
endif
```

```baan
ret = Create_CreateResponse.GetDataArea(response, da)                       |# 14
so.order = Create_DataArea.GetServiceOrder_v4(da)
service.order = Create_ServiceOrder_v4.GetserviceOrderCode(so.order))
xmlDelete(request)
xmlDelete(response)
request = ReleaseOrder_ReleaseOrderRequest.New()                            |# 15
ro = ReleaseOrder_ServiceOrder_v4.New(service.order)
da = ReleaseOrder_DataArea.New()
ret = ReleaseOrder_DataArea.AddServiceOrder_v4(da, ro)
ReleaseOrder_ReleaseOrderRequest.SetDataArea(request, da)
ret = BDE.ExecuteMethod("ServiceOrder_v4",                                  |# 16
"ReleaseOrder",
request,
response,
result,
exceptionmessage,
exceptionid)
if ret <> 0 then                                                            |# 13
abort.transaction()
message(exceptionmessage)
Exception.Delete(exceptionid)
return
endif
Exception.Delete(exceptionid)                                               |# 17
commit.transaction()                                                        |# 18
message(sprintf$("Service Order %s has been created and released.", service.order))
}
```

Explanation:
1   ottextextapi contains the functions for exception handling.
2   ottextbdeapi contains the function BDE.ExecuteMethod().
3   Transaction handling must always be in the calling program of the BDE method. Note that when you execute a BDE method in an extension hook (for example in the Before Save hook in a table extension, your hook must not start an own transaction, because it needs to be executed in the transaction of the program that calls the table extension.
4   This is the initialization of a new request that must be built up. Use always the functions from the proxy DLL with the method name followed by an “_” as prefix.
5   The example creates a Service Order. The root component is the Service Order itself and the component name is the same as the BDE name, ServiceOrder_v4 in this case. Because the Service Order number is a mandatory attribute of the Service Order, it must be passed as an argument. In this case the series in which the Service Order must be created.
6   Other attributes of the Service Order can be set as well. This also applies to the attributes of other components of the Service Order (Activity and Assignment Engineer) which are added later.
7   The Service Order is not directly connected to the request, but within the DataArea of the request. Here the DataArea is created, the Service Order is linked to it and the DataArea is connected to the request.
8   An Activity is created and
9   linked to the Service Order.
10 An Assignment Engineer is created and
11 linked to the Activity.
12 This is the call of the Public Interface to execute the BDE method to create the Service Order including the Activity and the Assignment Engineer. The XML request that has been built up by calling the functions is the proxy DLL looks like:
<Create.CreateRequest> <DataArea> <ServiceOrder_v4> <serviceOrderCode>JJD</serviceOrderCode> <serviceCenter>100</serviceCenter> <ServiceOrderActivity> <serviceOrderActivityPlannedStartTime>2019-05-03T07:22:35+02:00 </serviceOrderActivityPlannedStartTime> <serviceOrderActivityPlannedFinishTime>2019-05-03T08:22:35+02:00 </serviceOrderActivityPlannedFinishTime> <ActivityEngineer> <assignmentEngineer>0099101</assignmentEngineer> </ActivityEngineer> </ServiceOrderActivity> </ServiceOrder_v4> </DataArea> </Create.CreateRequest>
13 If the method fails, the transaction must be aborted. When the transaction is started outside your code (for example when your code is part of a table extension), you don’t need to abort, but return the error (DALHOOKERROR). The exceptionmessage field contains the most import message from the BDE method call. If you need more messages, you can use the Exception object (see public Interfaces for Extensibility) to retrieve the other messages.
14 Retrieve the generated Service Order Number from the response by getting the DataArea of the reponse XML document, getting the Service Order from the DataArea and then getting the Service Order Number attribute of the Service Order. The XML response of the Create method
looks like (the actual response contains much more elements, but they are left out for readability):
```baan
<CreateResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<DataArea>
<ServiceOrder_v4>
<serviceOrderCode>JJD000235</serviceOrderCode>
<customerOrderReference></customerOrderReference>
...
<ServiceOrderActivity>
<serviceOrderActivityLineNumber>10</serviceOrderActivityLineNumber>
<activityStatus>free</activityStatus>
<serviceOrderActivityPlannedStartTime>2019-05-03T05:22:35Z
</serviceOrderActivityPlannedStartTime>
<serviceOrderActivityPlannedFinishTime>2019-05-03T06:22:35Z
</serviceOrderActivityPlannedFinishTime>
```

```baan
...
<ActivityEngineer>
<assignmentLineNumber>1</assignmentLineNumber>
<assignmentStatus>assigned</assignmentStatus>
<assignmentEngineer>0099101</assignmentEngineer>
...
</ActivityEngineer>
</ServiceOrderActivity>
</ServiceOrder_v4>
</DataArea>
</CreateResponse>
```

15 Use this Service Order Number to build up the ReleaseOrder request.
16 Execute the ReleaseOrder method. If this method fails, the transaction needs to be aborted. In this case the created Service Order will be reverted as well.
17 Free the Exception object, which may contain information messages.
18 Commit the transaction. See also note 3 and 11.

## Process Extensions

Process Extensions are the opposite of Public Interfaces. Instead of calling standard LN methods (Public Interfaces) from the extensions, the standard LN application calls the Process Extensions, provided that they are implemented.
Process Extensions explained
With the extension types table extension, session extension, etc. the behavior and functionality of Infor LN can be changed in many ways (see the Infor LN Extensions Development Guide). But there may be additional requirements where intervening the standard functionality is required, which cannot be achieved with extending the table, session or any other component. Examples are processing and/or print sessions where additional selection ranges are required or core algorithms for composing invoices where the standard criteria are not sufficient, especially when customer defined fields need to be included in the selection and/or algorithm.
How to request a new Process Extension
The possibility to skip objects in processing and/or print sessions is a generic approach and can be used in every session where this Process Extension type has been implemented in the standard application. If you need to additional criteria whether or not objects may be processed by a session and that session has not been prepared for this Process Extension type, you can request this.
The other types of Process Extensions, where core algorithms can be extended, can be requested as well.
Apply the following process if you need a new Process Extension:
1   Evaluate if the request is generic. Make sure the required feature cannot be achieved with personalizing a standard session or process or by using one of the other extension points (for example a table extension).
2   In case of a skip Process Extension type, create an incident in the Infor Customer Portal. In case of another Process Extension type, create an enhancement request in Infor’s ERS system.
3   Infor Development will review the requested Process Extension and will either include it in the standard product or reject the request. If the Process Extension is developed it will be released via the regular delivery process.
4   After the new solution has been installed the customer can implement the new Process Extension using the extension modeler.
5   If an incident was created, Infor Support will complete the incident.
Available Process Extensions
The last chapter of this document describes the available Process Extensions for Infor LN (Cloud Edition) and how they must be implemented.
If the Process Extensions described in this document are not shown in the Extension Modeler in your environment, it may be necessary to apply a Knowledge Base article (KB) that can be found in the Infor Customer Portal. The applicable KB number is mentioned in the Process Extension description. Appendix A contains an overview of all Process Extensions per Infor LN Cloud release.

## Chapter 2 Public Interfaces for Extensibility

## Public Interfaces for Exception

The following functions are available: Exception.Delete Exception.GetMessage Exception.NumberOfMessages

## Exception.Delete

```baan
DLL:   tcextextapi
Syntax: Exception.Delete(
ref             long             ioExceptionID ) Usage:        Expl:   This function deletes the exception to free memory.
Pre:    ioExceptionID should refer to an Exception.
Post:   None
Input:
ioExceptionID   - the exception id.
Output:
ioExceptionID   - the exception id.
Return: None
```

## Exception.GetMessage

```baan
DLL:   tcextextapi
Syntax: Exception.GetMessage(
long             iExceptionID,
long             iMessageIndex,
ref     domain  tcmcs.s999m      oMessageDescription mb )
Usage:        Expl:   This function reads message description from all messages in
the XML identified by iExceptionID for a certain index.
Pre:    iExceptionID should refer to an Exception.
Post:   None
Input:
iExceptionID    - the exception id.
iMessageIndex   - the index for the message to be returned.
iMessageIndex should be greater than zero and
less than the number of messages.
Output:
oMessageDescription - The found message.
Return: None
```

## Exception.NumberOfMessages

```baan
DLL:   tcextextapi
Syntax: long Exception.NumberOfMessages(
long             iExceptionID ) Usage:        Expl:   This function determines the number if messages that have been
stored in the XML where iExceptionID refers to.
Pre:    iExceptionID should refer to a valid XML with the structure
as described above.
Post:   None
Input:
iExceptionID    - the exception id that points to the XML.
Output:
None
Return: The number of found messages. If iExceptionID does not refers
to a valid XML the return value is 0.
```

## Public Interfaces for ProcessingOptionSet

The following functions are available: ProcessingOptionSet.CheckOptionNames ProcessingOptionSet.Create ProcessingOptionSet.Delete ProcessingOptionSet.Read

## ProcessingOptionSet.CheckOptionNames

```baan
DLL:   tcextextapi
This function is available from 2026.06 (KB3668896).
Syntax: long ProcessingOptionSet.CheckOptionNames(
const           long             iProcessingOptionSet, ref     domain  tcmcs.s999m      oExceptionMessage mb, ref             long             oExceptionID, ... ) Usage:        Expl:   This function checks the validity of the given option-set, by
checking whether the option-set contains options that are *not*
provided in the variable arguments. The function can be used to
verify whether the option-set contains options that are not
supported.
Input:  iProcessingOptionSet    - reference to processing options set
Variable Arguments:
Repetition of argument:
OptionName      - option name of type string
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0       - Success
<> 0     - An error occurred
```

## ProcessingOptionSet.Create

```baan
DLL:   tcextextapi
This function is available from 2023.11 (KB2302509).
Syntax: long ProcessingOptionSet.Create(
ref             long             oProcessingOptionSet, ref     domain  tcmcs.s999m      oExceptionMessage mb, ref             long             oExceptionID, ... ) Usage:        Expl:   Create a Processing Option Set. The created Processing Option
Set can be used to control Public Interfaces that support this
functionality. Name/Value pairs must be given in the variable
arguments. Example flow for Item.Copy():
ret = ProcessingOptionSet.Create(
my.copy.item.processing.option.set,
my.exception.message1,
my.exception.id1,
"copyItemsBySiteAndItemsByOffice",      tcyesno.no,
"copyItemText",                         tcyesno.yes,
"copyReferenceDesignators",             tcyesno.no,
"targetItemDescription",  "This is the copied item",
"projectPartQuantity",                  751.12)
.
.
ret = Item.Copy(
source.item,
target.item,
my.copy.item.processing.option.set,
my.exception.message2,
my.exception.id2)
.
.
|* release memory
ret = ProcessingOptionSet.Delete(
my.copy.item.processing.option.set)
.
.
Pre:    -
Post:   Use ProcessingOptionSet.Delete() to release memory for the
allocated Processing Option Set.
Input:  Variable Arguments - repetition of pairs:
OptionName              - option name of type string
OptionValue             - option value, type as defined by
Public Interface usage.
Output: oProcessingOptionSet    - reference to the processing option set
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0               - successfully created
<> 0            - failed.
```

## ProcessingOptionSet.Delete

```baan
DLL:   tcextextapi
This function is available from 2023.11 (KB2302509).
Syntax: long ProcessingOptionSet.Delete(
ref             long             ioProcessingOptionSet ) Usage:        Expl:   Release memory for a created Processing Option Set/
Input/Output:   ioProcessingOptionSet - reference to Processing Option Set
Return:         0       - successfully deleted
<> 0    - failure.
```

## ProcessingOptionSet.Read

```baan
DLL:   tcextextapi
This function is available from 2026.06 (KB3668896).
Syntax: long ProcessingOptionSet.Read(
const           long             iProcessingOptionSet, ref     domain  tcmcs.s999m      oExceptionMessage mb, ref             long             oExceptionID, ... ) Usage:        Expl:   Assign default values to the options given and overwrite
from the Processing Option Set. The function
uses variable arguments to specify the options that may
be passed via this interface.
Note that no error is given if the Processing Option Set
contains an option that is not present in the argument triplets.
If consistency checking is required, then function
ProcessingOptionSet.CheckOptionNames in DLL tcextextapi can be
used.
Input:  iProcessingOptionSet    - reference to processing options set
Variable Arguments:
Repetition of sets of three arguments:
OptionName      - option name of type string
OptionVariable  - option variable (declared)
OptionDefault   - default option value, in type
of option variable
Output: Values of each OptionVariable is modified according to its
default option value or value from the Processing Option Set.
WARNING: When the domain of the output value has data type
String, it will NOT be aligned according to its
domain. To prevent unexpected results, alignment
can be programmed using tt.align.according.domain().
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0       - successfully read
<> 0     - failure
```

## Chapter 3 Public Interfaces for Common

## Public Interfaces for Address

The following functions are available: Address.Create Address.GetGPSData Address.StartDetail Address.StartPrintByBusinessPartner
