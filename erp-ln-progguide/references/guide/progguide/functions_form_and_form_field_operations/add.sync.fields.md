# add.sync.fields()

## Syntax:
`function void add.sync.fields( const string satelliteSessionCode, const string ... )`

## Description
This function maps a variable in the multi-main table controller session to a fields in the satellite session. This variable must be declared as external.
This function is relevant in multi-main table controller sessions only.

## Arguments
| | | |
|---|---|---|
| `const string` | `satelliteSessionCode` |  The session code of the satellite.  |
| `const string` | `...` |  Pairs of arguments of the form [const string variableName, const string satelliteField].  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Notes  The satellite session must have at least one index that looks like {static.mapping.field1, static.mapping.field2, ..., dynamic.mapping.field1, dynamic.mapping.field2, ..., useonce.mapping.field1, useonce.mapping.field2, ...}. Dynamic mapping fields are the fields added through add.sync.fields(). Useonce fields are the fields added through add.sync.fields.once().
This function can only be used in the after.form.read() section of the program script.

## Example
```

		extern domain tebme.long long.value
		extern domain tebme.title dyn.field.value

		after.form.read
			add.sync.fields("tebme0112m000", "long.value", "tebme012.long")
			long.value = 4
			add.sync.fields("tebme0113m000", "dyn.field.value", "tebme013.title")
			dyn.field.value = "DynamicTitleValue"
```

## Related topics
- [add.sync.fields.nokey()](add.sync.fields.nokey.md)
- [add.sync.fields.once()](add.sync.fields.once.md)
- [synchronize.satellite()](synchronize.satellite.md)
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
