# Specific Methods
The name of the specific method is built as follows:

- execute.<component name>.<method>()

- example: execute.Header.Approve()

- example without component: execute.Approve()

The system will generate the library. The file can be divided into two parts. The first part is read-only, while in the second part the content of the specific methods must be programmed (see the example below).

## Example Read-only
```

function extern long tlbct.bl790sf00.execute.Header.Approve()
{
    DllUsage
    EndDllUsage

    tlbct.bl790st00.get.Header.orderNumber(g.Header.orderNumber)

    RETIFNOK(execute.Header.Approve())

RETIFNOK(tlbct.bl790st00.set.Header.lifeCycle(g.Header.lifeCycle))

    return(0)
}

function extern long tlbct.bl790sf00.execute.Header.Present()
{
    DllUsage
    EndDllUsage

    tlbct.bl790st00.get.Header.orderNumber(g.Header.orderNumber)

    RETIFNOK(execute.Header.Present())

    RETIFNOK(tlbct.bl790st00.set.Header.present(g.Header.present))

    return(0)
}
```
Between the read-only and the development part the following 'comment' lines are present. The code below these lines will not be overwritten or removed during regeneration of the BOL.
```

|********** Below this line the specific function can be filled***************
|********** These lines will not be overwritten by Generation tool************
|********** REMARK : Changes above this line will be overwritten**************
|||SPECIFIC PART||| |* Do not remove this line!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

## To be filled by the developer
```

function long execute.Header.Approve()
{
    #pragma used dll otlbctdll7001

    RETIFNOK(tlbct.dll7001.approve.order(g.Header.orderNumber,
                         g.Header.lifeCycle))
        return(0)
}

function long execute.Header.Present()
{
    table   ttlbct700

    g.Header.present = false
    select  tlbct700.orno
    from    tlbct700
    where   tlbct700._index1 = {:g.Header.orderNumber}
    selectdo
        g.Header.present = true
    endselect

        return(0)
}
```

## Error Handling
In the development part, it is possible to report problems. The standard function 'dal.set.error.message' have to be used for setting an error message, followed by 'return (DALHOOKERROR)'.

## Related topics
- [Filter Hooks](filter_hooks.md)

- [Before and After Method Hooks](before_hooks.md)

- [Protected Layer](st_layer.md)
