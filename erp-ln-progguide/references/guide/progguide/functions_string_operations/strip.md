# strip$()

## Syntax:
`function string strip$( string str )`

## Description
This returns the specified string without trailing spaces. The input string remains unchanged.
Note that strip$() returns a reference to its argument, and not a copy of its argument. Therefore strip$(desc) is completely equivalent to desc(1;n), where n is the position of the last non-space character in desc.
Further note that this doesn't hold for multi language values. In this case strip$() returns either the unchanged original symbol or a modified copy.

## Arguments
| | | |
|---|---|---|
| `string` | `str` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

strip$("    ABC  ")      | result  "    ABC"
```

## Aliasing example
This is an artificial example, to show that strip$() returns a reference to its argument, instead of copying its argument.
```

string desc(100)

function void f(const string x)
{
    | at this point, x has value "BaanIVc"
    desc = "Infor Enterprise Server"
    | at this point, x has value "Infor E"
    ...
}

    ...
    desc = "BaanIVc"
    f(strip$(desc))
    ...
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
