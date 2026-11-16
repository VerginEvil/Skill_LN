# BOD.GetTextNumberFromNoteNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1672-1673

```baan
DLL:   tcextbodapi
This function is available from 2023.05 (KB2292786).
Syntax: long BOD.GetTextNumberFromNoteNode(
ref     domain  tcmcs.long       iXmlNode(),
domain  tcmcs.long       iSize,
domain  tcmcs.str50      iNoteType,
domain  tclang           iSystemLanguage,
ref     domain  tctxtn           ioTextNumber,
ref             boolean          oTextIsSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Based on iNoteType this function gets the text and creates a
text number with text or updates an existing text number with
the text provided in the Note elements in iXmlNode.
Example:
<Note type="Header" languageID="en">English text</Note>
<Note type="Header" languageID="nl">Dutch text</Note>
<Note type="Header" languageID="de">German text</Note>
<Note type="Footer" languageID="en">English Footer text</Note>
This function can be used to handle the texts of the inbound BOD.
The inbound BOD will take care of the transaction handling.
Pre:    The iXmlNode array must be intialized and filled before the
function call.
Post:   NA
Input:  iXmlNode                - Array with Note nodes. Mandatory.
iSize                   - Size of Notes array. Mandatory.
iNoteType               - Value of the type attribute in the
Notes array. If specified, only Notes
with this value and Notes without a
type attribute will be selected to
get the text.
iSystemLanguage         - If the languageID attribute is not
present in the Notes array, the
iSystemLanguage is used as fall back.
ioTextNumber            - Text number. If specified, this text
number is used. Otherwise a new text
number is generated.
Output: ioTextNumber            - The Text number that was updated or
created.
oTextIsSet              - Indicator if Text was updated/created
or not.
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
