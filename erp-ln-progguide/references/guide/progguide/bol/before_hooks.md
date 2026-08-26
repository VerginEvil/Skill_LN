# Before and After Method Hooks
In some cases the functionality of a standard method is not sufficient.
Therefore it should be possible to extend the standard behavior without moving the complete method to a specific method.
For a SalesOrder for instance a number of actions is needed after all order lines have been added or changed.
Each before/after hook has to be created manually in the development part of the script.
The name of the hook is built as follows:
- <dll name>befero|after.<method>()
- example: gaadv.bl090sf00.before.Create()  or specified for a component:
- <dll name>befero|after.<method><component name>()
- example: gaadv.bl090sf00.before.Create.Header()

## Example
```

function extern long gaadv.bl090sf00.after.Create()
{
    |* Next 4 lines are optional
    if gaadv.bl090st00.get.method.result() <> 0 then
        |* Execution of method has failed
        dal.set.error.message("@Execution of method Create has
failed.")
        return(DALHOOKERROR)
    endif

        .....

    return(0)
}
```

## Error Handling
In the development part, it is possible to report problems. The standard function 'dal.set.error.message' have to be used for setting an error message, followed by 'return (DALHOOKERROR)'.

## Related topics
- [Specific Methods](specific_methods.md)
- [Filter Hooks](filter_hooks.md)
- [Protected Layer](st_layer.md)
