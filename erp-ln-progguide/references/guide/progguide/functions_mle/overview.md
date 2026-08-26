# Multi Language Data overview
Infor Enterprise Server provides support to store multibyte strings - like descriptions - in multiple languages. System Administrators can define the Data Languages that can be used by end-users, as well as for which table fields it must be possible to enter the value in different languages. Note that the list of Data Languages is global and not per defined field.
E.g. if the item description field is defined as a Multi Language field in the database, and the Data Languages "eng" (English), "dut" (Dutch) and "ger" (German) have been defined, then an English user may create a new item with description "Bike", which can then be translated by a Dutch user to "Fiets", and by a German user to "Fahrrad". In this way English, Dutch and German users will see the item description in their own language.

## Concepts and Definitions
| | |
|---|---|
| *ISO 639 Language* | A 2 or 3 letter language code according to the ISO 639 standards. See http://www.loc.gov/standards/iso639-2/ for more information and a list of ISO 639 languages.  |
| *Data Language* | A Data Language is an ISO 639-2 Language like "eng" or a combination of an ISO 639.1 Language and ISO 3266.1 Country code like "en_US" which is actually used in the Infor Enterprise Server environment.  |
| *Base Language* | A Base Language is a special Data Language. Only one Base Language can be defined in the Infor Enterprise Server environent. It is used to determine the language of the user: if no Data Language is defined for the user, and no Data Language is defined for the Software Language of the user, then the Base Language is used. It is also used to support a 'fallback' mechanism in case a Multi Language value has not yet been translated into other languages.  |
| *Multi Language Field (MLF)* | A Multi Language Field is a database field of type multibyte string which can contain values in several Data Languages. Multi Language Fields are defined in sessions ttadv4137m000 Registered Table with Multi Language Fields and ttadv4138m000 Registered Multi Language Fields.  |
| *Multi Language Value (MLV)* | A Multi Language Value denotes the contents of a multibyte string variable. When Multi Language is enabled for the Infor Enterprise Server environment, conceptually *all* multibyte string variables (whether defined as MLF or not), will be treated as MLVs. This means that some of these variables conceptually will hold different translations (in case the contents is from a real Multi Language Field in the database) and some will hold the same translation for all defined Data Languages (in case the contents is from a single language field in the database).  |

## Change Data Language
A user can switch to another Data Language (if he is authorized to do so), via the Worktop/WebUI/LN UI Change Data Language option. This starts session ttdsk2006m000 Change Data Language. Changing a Data Language works similar to Changing a Company.

## Related topics
- [Multi Language Data synopsis](synopsis.md)
- [Multi Language Data support code examples](examples.md)
