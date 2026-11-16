# tt.languages()

## Syntax:
`function boolean tt.languages( boolean isolanguagecodes, ref long languages )`

## Description
This returns information about all available LN software languages.

## Arguments
```
<Languages>
	<Language>
		<LanguageCode>1</LanguageCode>
		<Description>Nederlands</Description>
		<IsoCode>nl-NL</IsoCode>
	</Language>
	<Language>
		<LanguageCode>2</LanguageCode>
		<Description>English</Description>
		<IsoCode>en-US</IsoCode>
	</Language>
	<Language>
		<LanguageCode>3</LanguageCode>
		<Description>Deutsch</Description>
		<IsoCode>de-DE</IsoCode>
	</Language>
</Languages>
```
| | | |
|---|---|---|
| `boolean` | `isolanguagecodes` |  If the iso codes for the languages (lowercase language - uppercase country) should be included.  |
| `ref long` | `languages` |  This returns all available LN software languages in XML format. The returned structure looks like:If isolanguagecodes is set to false, the IsoCode elements are not included.  |

## Return values
false error; no languages found
true success; languages found

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2150.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
