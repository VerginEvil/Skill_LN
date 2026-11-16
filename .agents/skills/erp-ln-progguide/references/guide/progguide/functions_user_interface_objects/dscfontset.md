# DsCfontSet

## Description
A DsCfontSet object defines a set of font attributes that other objects can apply to text strings. Objects indicate the font set to use by specifying the object ID of the font set in their DsNfontSet attribute.

## Events
A DsCfontSet object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNfsBaseline (long) | [G] | The height of the font (in pixels) relative to the baseline. This attribute corresponds to the MS Windows Ascent attribute. |
| DsNfsHeight (long) | [CG] | The height of the font, in pixels. When creating a font object, the height includes the internal leading. When retrieving information about a font object, the height excludes the internal leading. The default value is 12. |
| DsNfsMaWidth (long) | [G] | The maximum width of a (multibyte) character in pixels * 10. For nonproportional fonts, this attribute is identical to the DsNfsWidth attribute. |
| DsNfsPoints (long) | [G] | The height of the font in pixels * 10. This is the same value as returned by DsNfsHeight * 10. |
| DsNfsSlant (long) | [CG] | Possible values are: FNTROMAN FNTITALIC |
| DsNfsSpacing (long) | [CG] | The type of spacing. Possible values are: FNTFIXED Fixed spacing. FNTVARIABLE Proportional spacing. |
| DsNfsTypeface (string) | [CG] | The typeface name. For example, "Courier" or "MS Sans Serif". The following values have a special meaning: "DefaultFixed" Use a predefined default font with fixed width character spacing. "DefaultVariable" Use a predefined default font with proportional character spacing. If this attribute is not specified, or if it contains an empty string, BW uses the first font that matches the other specified attributes. |
| DsNfsWeight (long) | [CG] | The weight of the font. Possible values are: FNTMEDIUM FNTBOLD FNTNORMAL |
| DsNfsWidth (long) | [CG] | The average width of the font in pixels * 10. When neither DsNfsWidth nor DsNfsHeight are specified, the default is 8. When DsNfsWidth is not specified but DsNfsHeight is specified, the default width is DsNfsHeight/p. |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNstring (string) | [Q] | Use this attribute in a query operation to retrieve the height and width of the specified text string as displayed using the font set. The reply message contains the DsNwidth and DsNheight attributes of the string. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
