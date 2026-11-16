# mb.locale.enumerate()

## Syntax:
`function long mb.locale.enumerate( const string locale.name$ )`

## Description
This function returns information about one specific locale or about all locales.

## Arguments
| | | |
|---|---|---|
| `const string` | `locale.name$` |  Specifies the locale about which information is to be returned. If an empty string "" is supplied, information about all locales is returned.  |

## Return values
An XML tree containing the requested information.
Like any other XML tree, the returned tree must be freed from memory by using [xmlDelete](../functions_xml/delete_nodes.md).
When the supplied argument *locale.name$* refers to a not existing locale, e.g. "abcdefg", then the returned xml tree looks like this:
```

<enumeration
    type="locales"
    name="abcdefg"
/>
```
When the supplied argument refers to an existing locale, e.g. "ISO88591_WIN32", then the returned xml tree looks like this:
```

<enumeration
    type="locales"
    name="ISO88591_WIN32">
    <locale
        name="ISO88591_WIN32"
        nlsname="NULL"
        tssname="CP1252"
        tss_characterset_id="7"
        internal_factor="1"
        external_factor="1"
        multibyte="false"
        language_group="Latin1"
    />
</enumeration>
```
When the supplied argument *locale.name$* is an empty string "", then the returned xml tree contains a <locale> node for each existing locale, and looks like this:
```

<enumeration
    type="locales">
    <locale
        name="GB2312_WIN32"
        nlsname="chs"
        tssname="CP936"
        tss_characterset_id="17"
        internal_factor="2"
        external_factor="2"
        multibyte="true"
        language_group="Simplified Chinese"
    />
    <locale
        name="ISO88591"
        nlsname="NULL"
        tssname="ISO88591"
        tss_characterset_id="0"
        internal_factor="1"
        external_factor="1"
        multibyte="false"
        language_group="Latin1"
    />

    ... etcetera ...

    <locale
        name="ISO_BIN5"
        nlsname="NULL"
        tssname="ISO88595"
        tss_characterset_id="23"
        internal_factor="1"
        external_factor="1"
        multibyte="false"
        language_group="Cyrillic"
    />
</enumeration>
```
The 'name' attribute corresponds to the locale name as returned by [mb.localename$()](mb.localename.md).
The five attribute names 'name', 'nlsname', 'tssname', 'internal_factor', and 'external_factor' correspond to the five values 'TSS_GET_LOCALE_NAME', 'TSS_GET_NLS_NAME', 'TSS_GET_TSS_NAME', 'TSS_GET_IFACTOR', and 'TSS_GET_EFACTOR' of the flag supplied to the function [mb.locale.info()](mb.locale.info.md).
The attributes 'tss_characterset_id' and 'tssname' correspond to the first two arguments of [mb.set.info()](mb.set.info.md).
The attribute 'tss_characterset_id' corresponds to the value returned by [mb.char.info()](mb.char.info.md) and to the optional third argument of [mb.import$()](mb.import.md), [mb.import.raw()](mb.import.raw.md), [mb.export$()](mb.export.md), and [mb.export.raw()](mb.export.raw.md).
The attribute 'multibyte' indicates if the locale has a multibyte native encoding.
All locales that share a common character set have the same 'language_group' attribute.

## Context
This function is implemented in the porting set and can be used in all script types.
Availability  The attributes "multibyte" and "language_group" are available from TIV 1700.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
