# ask.enum()

## Syntax:
`function bset ask.enum( string quescode, bset default_enumval, [ void arg, ... ] )`

## Description
This displays a message box containing a question and a number of possible responses. The responses are presented as push buttons. To respond to the question and close the message box, the user selects one of the push buttons.
The possible responses are defined in the data dictionary as an enumerated domain. By default, the function displays all of the defined enumerate values. To display a subset only, call [set.ask.enum.values()](set.ask.enum.values.md) before calling *ask.enum()*.

## Arguments
| | | |
|---|---|---|
| `string` | `quescode` |  The question to be displayed in the message box is defined in the data dictionary. This argument specifies the data dictionary code for the question. If the question contains substitution symbols, use the third and subsequent arguments to specify the values to substitute for these symbols.  |
| `bset` | `default_enumval` |  Specifies the enumerate value of the default answer. For example, tcyesno.yes. If this argument is empty, the default value specified in the data dictionary is used.  |
| `[ void` | `arg, ... ]` |  The values to substitute for any substitution symbols that the question contains. See [sprintf$()](../functions_formatting_io/sprintf.md).  |

## Return values
The value of the enumerated domain that corresponds to the option selected by the user. This is always the enumerate value and not its description.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and Value of argument quescode starts with "tx"    Notes  The question text and the push button labels are always in the language of the user. The return value of *ask.enum()* is always the enumerate value and not its description. So the script in which the function is used remains language independent.
The process executing this function should have a UI. In job processes this function will stop the session.

## Example
This example assumes an enumerated domain 'tcyesno' with two possible constants: 'tcyesno.yes' and 'tcyesno.no'. It also assumes a question defined in the data dictionary with code "tccom00001". This question contains the string "Error %d in file %s; Try again [y/n]?". The default answer is yes.
```

ret = seq.open( filename, "w" )
while ( ret <= 0 )
    if ( ask.enum( "tccom00001", tcyesno.yes, ret, filename )
                  = tcyesno.no) then
         return
    endif
    ret = seq.open( filename, "w" )
endwhile
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)
- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
