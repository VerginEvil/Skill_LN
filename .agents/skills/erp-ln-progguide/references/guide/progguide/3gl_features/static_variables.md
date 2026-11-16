# Static variables
You can declare local variables as static variables. The value of a static variable is saved at the end of the function and is used again the next time the function is called. A static variable is automatically initialized at the start of the program. Normal local variables are undefined at each function call, and are not initialized at first call.

## Declaration, initialization, and scope
| | |
|---|---|
| Point of declaration | In the function between the brackets { }. |
| Syntax of declaration | static <type> name |
| Initialization | At program start: numeric set to 0 boolean set to false strings "" |
| Scope (validity and time) | Can be used only within the function but they maintain their values throughout program execution. |

## Example 1
```

function test()
{
        static boolean started

        if (not started) then
                started = true
                | Actions to be performed only first time around.
        endif
        ...
        return
}
```

## Example 2
```

function void spool( long id, ref string line() )
{
        static long   save_id
        static long   lfn

        if ( save_id <> id ) then      | Optimization
                lfn = read_new_lfn( id )
                save_id = id
        endif
        seq.puts( line, lfn )
}
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Functions](functions.md)
