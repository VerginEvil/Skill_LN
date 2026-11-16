# TestData.Update

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for TestData
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1801-1802

```baan
DLL:   qmextptcapi
This function is available from 2025.08 (KB3549688).
Syntax: long TestData.Update(
domain  qmptc.iorn       iInspectionOrder,
domain  tcpono           iInspectionLine,
domain  qmptc.saml       iSample,
domain  qmptc.srno       iSamplePart,
domain  qmptc.limt       iMeasurementValue,
domain  qmptc.optn       iOption,
domain  qmptc.tare       iTestArea,
domain  tcemno           iAssignedEmployee,
domain  qmptc.inst       iInstrument,
domain  qmptc.iorn       iInstrumentNumber,
domain  tcyesno          iResetMeasurementValue,
domain  tcyesno          iUpdateAlgorithmAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function will update the Test Data.
Pre     : db.retry.point has to be set before calling this function.
Post    : commit.transaction() or abort.transaction should be done.
Input   : iInspectionOrder : Inspection order, Mandatory.
iInspectionLine  : Inspection Line, Mandatory.
iSample          : Sample, Mandatory.
iSamplePart      : Sample Part,
Mandatory: In case of Inspection Order is
Not a Conformance Reporting.
iMeasurementValue: Measurement Value,
1. The input value is considered only if the Result Type
of the given Inspection Order Line is Quantitative.
2. The input value can be Zero.
In this case Test Data will be updated based on input
field iResetMeasurementValue.
3. Therefore, The Result will be either calculated or
reset.
iOption          : Option,
1. The input value is considered only if the Result Type
of the given Inspection Order Line is Qualitative.
2. The input value is Mandatory when Result Type is
Qualitative.
iTestArea        : Test Area, Optional.
iAssignedEmployee: Assigned Employee, Optional.
iInstrument      : Instrument, Optional.
iInstrumentNumber: Instrument Number, Optional.
iResetMeasurementValue : Reset Measurement Value,
The input value is considered only in case of
Measurement Value is Zero.
Because, it can have two meanings:
1. The user has not yet measured the characteristic
and wants to reset the test data. (or)
2. The measured value of the characteristic is really
Zero.
Therefore, the Possible Input values are,
Yes: Reset the Measurement value and Result.
No : The Measured Value is Zero.
iUpdateAlgorithmAllowed: In case the Test Data of a given
Inspcetion Order Line is used in Algorithm of another
Order Line which has Test Data for same Inspection Order
and Sample, then this Input will indicate that,
The Measuremt value and Test Data is allowed to
update or not.
Therefore, the Possible Input values are,
Yes: Update the Measurement Value and Test Data.
No : Do Not Update the Measurement Value and Test Data.
Output  : oExceptionMessage     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No Error.
<> 0                    - Error found.
```
