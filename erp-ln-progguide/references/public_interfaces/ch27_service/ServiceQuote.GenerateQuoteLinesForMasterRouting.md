# ServiceQuote.GenerateQuoteLinesForMasterRouting

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1475-1475

```baan
DLL:   tsexteppapi
This function is available from 2024.08 (KB3511976).
Syntax: long ServiceQuote.GenerateQuoteLinesForMasterRouting(
domain  tcorno           iQuote,
domain  tcpono           iQuoteRevision,
domain  tsbsc.clst       iInstallationGroup,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tsacm.cact       iMasterRouting,
domain  tsacm.cact       iRoutingOption,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles generating Quote Lines under a Quote based
on a Master Routing similar to process session Generate Lines
for Master Routing (tsepp1210m000).
Pre:    A db.retry.point() must have been specified.
Post:   An abort.transaction() or commit.transaction() must be executed.
Input:  iQuote
Service Quote (mandatory)
iQuoteRevision
Service Quote Revision (optional)
iInstallationGroup
Installation Group to generate Quote Lines for (optional)
iItem
Item to generate Quote Lines for (optional)
iSerialNumber
Serial Number of Serialized item to generate Quote
Lines for (optional)
iMasterRouting
The Master Routing to use (mandatory)
iRoutingOption
The Routing Option of the Master Routing to use
(optional). Note that the Master Routing needs to have a
default Routing Option or at most one Routing Option if
this is omitted.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - Quote Lines generated successfully.
<> 0    - Error during generating of Quote Lines.
```
