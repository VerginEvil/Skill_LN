# BOD.CreateLastModificationPersonNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1659-1660

```baan
DLL:   tcextbodapi
This function is available from 2023.05 (KB2292786).
Syntax: long BOD.CreateLastModificationPersonNode(
domain  tcmcs.str50      iLogonCode,
ref     domain  tcmcs.long       oXmlNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a LastModificationPerson node based on
the iLogonCode.
The current LN user (logname$) is used instead of iLogonCode if:
- Input variable iLogonCode is empty.
- Length of input variable iLogonCode is greater than
length of domain 'tclogn' (string 16).
- The iLogonCode does not exist as LN User.
The LastModificationPerson node is not created if this function
is called in company 0 or if no employee exists for iLogonCode
in the Employee (tccom001) table. In this case oXmlNode is
returned as 0 and the return value of the function is 0.
XML structure:
<LastModificationPerson>
<IDs>
<ID
accountingEntity="aaa"
location="bbb"
lid="ccc">xxx</ID>
<Name>
</LastModificationPerson>
Pre:    NA
Post:   NA
Input:  iLogonCode              - The logon code of the LN User
Output: oXmlNode                - Generated Node
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Error occurred.
```
