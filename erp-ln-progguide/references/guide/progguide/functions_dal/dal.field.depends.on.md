# dal.field.depends.on()

## Syntax:
`#include <bic_dal>`
`function void dal.field.depends.on( const string fieldname, long hook.list, const string parent.fld.name, ..., [ long hook.list, const string parent.fieldname, ... ] )`

## Description
Use this to define that a field depends on one or more other fields. Dependencies are defined in terms of field hooks.
In general `dal.field.depends.on("a", HOOK_X, "b")` means the following: the result of hook a.x() depends on the value of field b.
So when changing field "b", hook a.x() is executed.
For example, `dal.field.depends.on("whinh312.fire", HOOK_IS_VALID, "whinh312.lsta")` should be used if the result of hook whinh312.fire.yes.is.applicable() depends on the value of whinh312.lsta.

## Arguments
| | | |
|---|---|---|
| `const string` | `fieldname` |  the field that depends on other fields  |
| `long` | `hook.list` |  the hooks that use the parent fields that follow The following hook constants can be used:  |
| `const string` | `parent.fld.name, ...` |  one or more fields on which the given field (fieldname) depends  |
| `[ long` | `hook.list ]` |  |
| `[ const string` | `parent.fieldname, ... ]` |  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.
Note  Sometimes there are 'indirect' dependencies, e.g., through database references. For example, suppose that table field teemp100.emno refers to tccom001.emno, that tccom001.awak is read through the DAL query extension of DAL teemp100, and that the result of teemp100.talk.update() uses tccom001.awak. In that case there is an 'indirect' dependency, and the following dependency should be defined: `dal.field.depends.on("teemp100.talk", HOOK_UPDATE, "teemp100.emno")`.
Note  The defined dependencies are uni-directional. So in order to specify a bi-directional relation, i.e., when A depends on B and B depends on A, you have to call this function twice:
- dal.field.depends.on("A", HOOK_UPDATE, "B")
- dal.field.depends.on("B", HOOK_UPDATE, "A")  This function can only be called in the [before.open.object.set()](before.open.object.set.md) hook!

## Example
Suppose field G depends on fields D, E and F and field D is used in the is.applicable hook, field E is used in the is.readonly hook and field F is used in both the is.applicable and update hooks then this is coded as follows:
```

dal.field.depends.on("G",
        HOOK_IS_APPLICABLE,               "D",
        HOOK_IS_READONLY,                 "E",
        HOOK_IS_APPLICABLE + HOOK_UPDATE, "F")
```
It is also possible to use the following syntax:
```

dal.field.depends.on("G",
        HOOK_IS_APPLICABLE, "D", "F",
        HOOK_IS_READONLY,   "E",
        HOOK_UPDATE,        "F")
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
- [DAL2 Field dependencies](dal2_field_dependencies.md)
- [dal.require.field()](dal.require.field.md)
- [dal.any.parent.changed()](dal.any.parent.changed.md)
