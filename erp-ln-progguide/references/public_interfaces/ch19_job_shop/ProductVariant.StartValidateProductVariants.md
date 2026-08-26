# ProductVariant.StartValidateProductVariants

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 687-688

```baan
DLL:   tiextpcfapi
This function is available from     2024.10 (KB3526537  ).
Syntax: long ProductVariant.StartValidateProductVariants(
long             iStartMode,
domain  tccpva           iProductVariantFrom,
domain  tccpva           iProductVariantTo,
domain  tccom.bpid       iBusinessPartnerFrom,
domain  tccom.bpid       iBusinessPartnerTo,
domain  tcyesno          iOverwriteSalesPrice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to start process session
Validate Product Variants(tipcf5200m000).
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS                               -
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dailog.
iProductVariantFrom
From Product Variant                               - Optional.
The default is the minimum domain value
iProductVariantTo
To Product Variant                               - Optional.
The default is equal to iProductVariantFrom if it is
given. The maximum domain value otherwise.
iBusinessPartnerFrom
From Business Partner                               - Optional.
The default is the minimum domain value.
iBusinessPartnerTo
To Business Partner                               - Optional.
The default is equal to iBusinessPartnerFrom if it is
given. The maximum value otherwise.
iOverwriteSalesPrice
Control to overwrite the sales price                               - Optional
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       Session started
<> 0    Error Occurred
```
