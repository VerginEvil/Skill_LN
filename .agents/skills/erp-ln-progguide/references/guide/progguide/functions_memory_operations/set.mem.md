# set.mem()

## Syntax:
`function long set.mem( ref void destination, void source, [ long count ] )`

## Description
The stores the value of *source* in the *destination* argument. By default, the value of *source* is repeated in *destination* until the latter is completely filled. Use the optional *count* argument to repeat the value of *source* a specific number of times only. Elements in the *destination* argument which are not overwritten remain unchanged.

## Arguments
| | | |
|---|---|---|
| `ref void` | `destination` |    |
| `void` | `source` |    |
| `[ long` | `count ]` |    |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| To set a string array to spaces
        string string_array(20, 5, 5)
        long ret
        ret = set.mem( string_array, "" )

| To store a long in a string
        string str1(20)
        long ret
        ret = set.mem( str1, "10", 5 )
                | str1 now contains "1010101010"
```

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
