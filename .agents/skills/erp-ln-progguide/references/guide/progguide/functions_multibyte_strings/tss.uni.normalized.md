# tss.uni.normalized$()

## Syntax:
`function string tss.uni.normalized$( const string source$, long tss.uni.normalization.form )`

## Description
Normalize the supplied *source$* string according to the specified normalization form and return the result.

## Arguments
| | |
|---|---|
| named constant | meaning |
| TSS_UNI_NORMALIZATION_FORM_C | Use Unicode Normalization Form C (NFC): Canonical Decomposition, followed by Canonical Composition. |
| TSS_UNI_NORMALIZATION_FORM_D | Use Unicode Normalization Form D (NFD): Canonical Decomposition. |
| TSS_UNI_NORMALIZATION_FORM_KC | Use Unicode Normalization Form KC (NFKC): Compatibility Decomposition, followed by Canonical Composition. |
| TSS_UNI_NORMALIZATION_FORM_KD | Use Unicode Normalization Form KD (NFKD): Compatibility Decomposition. |
Unicode Normalization according to Normalization Form C (NFC) is implicitly applied at several points at the boundaries of the Infor ES system, with the intention that strings inside the system are in Normalization Form C. Examples of such points are:

- string conversion from Unicode (UTF-8 or UTF-16) to TSS (see [uni.import()](uni.import.md) and [utf8.import()](utf8.import.md));

- xml de-serialization (see [xmlRead()](../functions_xml/de_serialize_xml_object.md), [xmlReadFromString()](../functions_xml/de_serialize_xml_object_string.md), [xmlReadNs()](../functions_xml/xmlReadNs.md), and [xmlReadFromStringNs()](../functions_xml/xmlReadFromStringNs.md)).

## Return values
| | |
|---|---|
| <> "" | Success. A multibyte string, containing a copy of the supplied *source$* string, normalized according to the specified normalization form. |
| "" | Error. The supplied *tss.uni.normalization.form* is not one of the valid normalization form values. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
