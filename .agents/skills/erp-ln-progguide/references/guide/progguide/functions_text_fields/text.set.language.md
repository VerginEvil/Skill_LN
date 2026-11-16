# text.set.language()

## Syntax:
`function boolean text.set.language( string text_field, string language, void... )`

## Description
This function changes the language for multiline textfields that are displayed on the form and are part of the maintable. That language will be used when (one of) the textfields are/is read from the text tables. The language that is set with this function can still be overridden by setting attr.textlang$ in the before.choice section for the text.manager.
If this function is called after one of the texts is changed in a multiline text formfield, then the record is saved first (with the text in the current language). After the language is set the text is read from the database in the new language, but not displayed on the form yet. You can use function display(<text_field>) to display the text in the multiline text formfield.
Field names and language codes must be provided in pairs.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the textfield for which the language must be set.  |
| `string` | `language` |  The language code.  |
| `void` | `...` |    |

## Return values
false some error occurred
true function successful

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  You cannot use the function in any subsection of *choice.update.db* and in the field sections of the multiline text fields.

## Example
```

    ret = text.set.language("ttadv151.docu", "3",
                "ttadv151.help", "1")
```

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
