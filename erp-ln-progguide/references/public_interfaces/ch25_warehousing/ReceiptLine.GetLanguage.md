# ReceiptLine.GetLanguage

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1255-1255

```baan
DLL:   whextinhapi
This function is available from 2023.10 (KB2304631).
Syntax: long ReceiptLine.GetLanguage(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
boolean          iConvertToSystemLanguage,
ref     domain  tcclan           oLanguage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to determine the language for printing
receipt text and inspection text.
Depending on the order origin, the receipt text is entered by
default in the company language, Business Partner language or
Order Header Language.
This function returns the proper language code in which the
receipt text (whinh312.txtn) and inspection text (whinh312.itxt)
will be printed. The same applies to printing the Inspection
Text (whinh211.itxt).
Pre:    N.a.
Post:   N.a.
Input:  iReceipt - Receipt number (Mandatory)
iReceipt - Receipt line (Mandatory)
iConvertToSystemLanguage - Convert to internal language
(true/false)
Output: oLanguage - The language code for the receipt
Return: 0: OK
<> 0: Error
```
