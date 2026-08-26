# User.ConvertToRuntime

> Chapter: Chapter 51 Public Interfaces for User Management
>
> Group: Public Interfaces for User
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1937-1939

```baan
DLL:   ttextaadapi
This function is available from     2025.06 (KB3601093  ).
Syntax: long User.ConvertToRuntime(
const   domain  ttaad.user       iUser,
const           boolean          iUserData,
const           boolean          iRemoteUserData,
const           boolean          iDevicePreferences,
const           boolean          iDevelopmentParameters,
const           boolean          iDeveloperAuthorizations,
ref             string           oExceptionMessage() mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface converts User Data to runtime. The functionality
is the same as the Convert action in session User Data (ttaad2500m000).
Transaction management is handled internally in this Public Interface.
Pre:    No transaction active.
User must be able to switch to company 0.
Post:   None.
Input:  iUser                                  - The User which must converted to runtime.
Mandatory and must exist in the database.
iUserData                                      - If this option is selected, the user data,
terminal authorizations and text group
authorizations are converted to run time.
Mandatory (true/false).
iRemoteUserData                                - If this option is selected, the remote user
data are converted to run time.
Mandatory (true/false). Is ignored in Cloud
Edition.
iDevicePreferences                             - If this option is selected, the device
preferences are converted to run time.
Mandatory (true/false).
iDevelopmentParameters                         - If this option is selected, the development
parameters are converted to run time.
Mandatory (true/false).
iDeveloperAuthorizations                       - If this option is selected, the developer
authorizations are converted to run time.
Mandatory (true/false).
Output: oExceptionMessage                      - A message if the return value is not equal
to 0. This message contains the root cause of
the of the method failure.
oExceptionID                                   - An ID that refers to all error information. Use
the functions in Exception to get the error
messages.
Return values:
0                                              - Function is executed successfully
<> 0                                           - Error(s) occurred
```

## Chapter 52 Public Interfaces for Document Output

## Management

## Public Interfaces for Documents

The following functions are available: Documents.StartOverview
