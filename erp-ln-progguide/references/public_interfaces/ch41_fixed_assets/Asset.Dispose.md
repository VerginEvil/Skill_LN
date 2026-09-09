# Asset.Dispose

> Chapter: Chapter 41 Public Interfaces for Fixed Assets
>
> Group: Public Interfaces for Asset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1837-1838

```baan
DLL:   tfextfamapi
This function is available from 2026.04 (KB3652514).
Syntax: long Asset.Dispose(
domain  tcncmp           iAssetCompany,
domain  tffam.mcod       iAssetNumber,
domain  tffam.mcod       iAssetExtension,
domain  tfgld.date       iDisposalDate,
domain  tffam.code       iReason,
domain  tffam.dtyp       iDisposalType,
domain  tfgld.perc       iDisposalPercentage,
domain  tfgld.amnt       iDisposalAmount,
domain  tffam.pzlg       iDisposalQuantity,
domain  tcyesno          iProceedWithoutGainLoss,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function disposes an asset.
Input:  iAssetCompany           - Asset Company: Mandatory
iAssetNumber            - Asset Number: Mandatory
iAssetExtension         - Asset Extension: Mandatory
iDisposalDate           - Disposal Date: Mandatory
iReason                 - Reason: Mandatory
iDisposalType           - Disposal Type: Mandatory
iDisposalPercentage     - Disposal Percentage
iDisposalAmount         - Disposal Amount
iDisposalQuantity       - Disposal Quantity
iProceedWithoutGainLoss - Proceed without Gain/Loss: Mandatory
iProcessingOptionSet    - Mandatory, a Processing Option Set
can be created via a call to
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Dispose Assets (tffam8240m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
Options which are not available as Processing Options will get
defaulted with the value in column DEFAULT below.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
DisposalBook            domain  tffam.mcod      empty
DisposalBusinessPartner domain  tccom.bpid      empty
Suppress                domain  tcyesno         tcyesno.no
ProceedAmount           domain  tfgld.amnt      zero
ProceedCurrency         domain  tcccur          local currency of
iAssetCompany
Location1From           domain  tffam.lcod      minimum value
Location1To             domain  tffam.lcod      maximum value
Location2From           domain  tffam.lcod      minimum value
Location2To             domain  tffam.lcod      maximum value
Location3From           domain  tffam.lcod      minimum value
Location3To             domain  tffam.lcod      maximum value
Location4From           domain  tffam.lcod      minimum value
Location4To             domain  tffam.lcod      maximum value
Location5From           domain  tffam.lcod      minimum value
Location5To             domain  tffam.lcod      maximum value
Location6From           domain  tffam.lcod      minimum value
Location6To             domain  tffam.lcod      maximum value
Location7From           domain  tffam.lcod      minimum value
Location7To             domain  tffam.lcod      maximum value
Location8From           domain  tffam.lcod      minimum value
Location8To             domain  tffam.lcod      maximum value
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
