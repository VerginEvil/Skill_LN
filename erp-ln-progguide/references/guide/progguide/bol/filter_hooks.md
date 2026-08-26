# Filter Hooks
In several cases data from the Database must be hidden. In Baan ERP UI this can be programmed via specific query extends in the UI-script or in the DAL. This means that an end-user will never see certain data.
This mechanism is also present for retrival methods like List and Show, where objects or parts of objects can be hidden for end-users or a client application.
This is called BO filtering.
Since BO filters are application specific, the filters are part of the specific hooks in the Protected Layer of the BOL. The hooks for object filters must be specified per BO component.
Each filter hook has to be created manually in the development part of the script.
The name of the hook is built as follows:
- <dll name>.<component name>.object.filter()
- example: gaadv.bl090sf00.Header.object.filter()
- example without component: gaadv.bl091sf00.object.filter()

## Typical example
When a List or Show is executed on BO 'SalesOrder' (tdsls040), objects that are canceled will never be shown.
```

tdsls.bl040sf00.Header.object.filter(
                    ref string  oComponentFilter)
{
    |* Do not allowed reading canceled Sales Orders
    oComponentFilter = "tdsls400.clyn <> tcyesno.yes"
}
```

## Related topics
- [Specific Methods](specific_methods.md)
- [Before and After Method Hooks](before_hooks.md)
- [Protected Layer](st_layer.md)
