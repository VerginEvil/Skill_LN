# BOD.PublishLNMessage

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1658-1660

```baan
DLL:   tcextbodapi
This function is available from     2019.03 (KB2040021  ).
Syntax: long BOD.PublishLNMessage(
domain  tcmcs.str30m     iMessageType mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This function publishes the LnMessageBOD with a specific MessageType.
The first three arguments are mandatory, in the given order.
iMessageType can f.i. have value "PurchaseScheduleLine".
The other arguments should be 'xml_elementname                       - xml_elementvalue'
pairs, e.g.:
"Description",          tfgld011.desc,
The number of input arguments can vary.
The DocumentID is mandatory as one of the xml_element names:
"DocumentID",           table.key1,
"DocumentID",           table.key2,
The maximum composed DocumentID_ID string length is 132.
If the "ActionCode" is not set, the default "Add" is used.
If "DisplayID" is not set the "DocumentID" is used to create the
DisplayID.
To create a user area node a UserAreaName, UserAreaType and
UserAreaValue are mandatory. UserAreaDescription,
UserAreaStartDate and UserAreaEndDate can also be used.
--                      > In the function call, the same order must be used!
Allowed values for UserAreaType are:
-                            "DateTimeType"
-                            "IndicatorType"
-                            "NumericType"
-                            "StringType"
If an xml_elementname is not in the list of possible
xml_elementnames, the xml_element value is added to the
"MessageTypeDetails" node, e.g.:
input arguments:
"MessageType"           "TestType",
"Element.1"             field.1,
"Element.2"             field.2,
result node:
<MessageTypeDetails>
<TestTypeGroup>
<Element.1>field.1</Element.1>
<Element.2>field.2</Element.2>
</TestTypeGroup>
</MessageTypeDetails>
xml_elementvalues should apply to the following rules:
utc dates should be converted to string representation in ISO.
e.g.: "EffectiveDateTime",      utc.to.iso(datefield, UTC_ISO_Z)
Use the english description associated with a specific value
in an enumerated domain.
e.g.:   "TransactionCategory",  enum.descr$("tfgld.catg",
tfgld011.catg,
"2")
Attributes of an xml_element are reflected using an @ and
must be placed directly under the xml_element on which they
are related, e.g.:
"PurchaseInvoiceAmount",                "10.000",
"PurchaseInvoiceAmount@currencyID",     "EUR",
<PurchaseInvoiceAmount currencyID="EUR">10.000
</PurchaseInvoiceAmount>
Possible xml_element names:
-                            "ActionCode"
-                            "Authorization"
-                            "Description"
-                            "DocumentReference"
-                            "DocumentReference_ID"
-                            "DocumentReference_LineNumber"
-                            "DocumentReference_ScheduleLineNumber"
-                            "DisplayID"
-                            "DistributionGroup_Contact"
-                            "DistributionGroup_ContactGroup"
-                            "DistributionGroup_Email"
-                            "DistributionGroup_Person"
-                            "DistributionGroup_PersonGroup"
-                            "DocumentID"
-                            "Message_Description"
-                            "Message_ID"
-                            "MessageType"
-                            "Note" (the xml_element value must be a text number)
-                            "Status_Code"
-                            "Status_EffectiveDateTime"
-                            "Status_ArchiveIndicator"
-                            "UserAreaDescription"
-                            "UserAreaEndDate"
-                            "UserAreaName"
-                            "UserAreaStartDate"
-                            "UserAreaType"
-                            "UserAreaValue"
Pre:    Transaction handling is needed.
Post:   Transaction handling is needed: A commit or abort must be done.
Input:  iMessageType: Mandatory
Variable arguments are pairs of two arguments with
name and value. At least one argument with name "DocumentID"
is Mandatory.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - BOD is published.
<> 0                                          - BOD could not be publised.
```
