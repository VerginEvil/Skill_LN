# BOD.CreateNoteNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1641-1642

```baan
DLL:   tcextbodapi
This function is available from     2023.05 (KB2292786  ).
Syntax: long BOD.CreateNoteNode(
domain  tctxtn           iTextNumber,
domain  tcmcs.str50      iNoteType,
ref     domain  tcmcs.long       ioXmlNode(),
ref     domain  tcmcs.long       ioSize,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Based on iTextNumber this function creates one or more Note nodes
with iNoteType as attribute.
The number of nodes created depends on the number of languages
for which the text has been defined.
<Note type="Header" languageID="en">English text</Note>
<Note type="Header" languageID="nl">Dutch text</Note>
<Note type="Header" languageID="de">German text</Note>
This function can be called multiple times; each time with a
different value for iTextNumber and iNoteType. New Note nodes
will be appended to the existing array with Note nodes.
Result for first call with iNoteType is "Header":
<Note type="Header" languageID="en">Header text</Note>
Result for second call with iNoteType is "Footer":
<Note type="Header" languageID="en">Header text</Note>
<Note type="Footer" languageID="en">Footer text</Note>
Pre:    The ioXmlNode array must be intialized as based before the
function call:
long    ioXmlNode(1)    based
Post:   NA
Input:  iTextNumber                           - Text number. Mandatory.
iNoteType                                     - Value for the type attribute in the
generated Note nodes. This is mandatory
if the function is called multiple
times for the same ioXmlNode array.
Otherwise, optional.
ioXmlNode                                     - Existing Notes array; new nodes will
be appended.
ioSize                                        - Size of existing ioXmlNode array.
Output: ioXmlNode                             - Result with Note nodes.
ioSize                                        - Size of ioXmlNode array.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK.
<> 0                                          - Error occurred.
```
