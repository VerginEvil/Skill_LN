# Interface Conversion Public Layer
In this library the logic of the public calculated fields must be programmed in specific hooks:
- function long public.{all|<attribute>}.map.to.<attribute>()
- function long public.<attribute>.map.from.{all|<attribute>}()   'all' will be used when more then one protected attribute has been mapped to the public attribute. Normally the mapped attribute will be filled out in <attribute>.
The system will generate the library. The file can be divided into two parts. The first part is read-only, while in the second part the content of the hooks must be programmed (see the example below).

## Example Read-only
```

function extern long tlbct.bl790sc00.set.material(
                    const domain tlst40 i.value)
{
    DllUsage
    EndDllUsage

    g.public.material = i.value
    g.public.material.set = true

    RETIFNOK(tlbct.bl790st00.get.Line.item(
                g.item))
    g.item.set = true
    RETIFNOK(public.all.map.to.item())

    RETIFNOK(tlbct.bl790st00.set.Line.item(
                g.item))

    return(0)
}

function extern long tlbct.bl790sc00.get.material(
                    ref domain tlst40 o.value)
{
    DllUsage
    EndDllUsage

    RETIFNOK(tlbct.bl790st00.get.Line.item(
                g.item))
    g.item.set = true
    RETIFNOK(public.material.map.from.item())
    o.value = g.public.material
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

function long public.all.map.to.item()
{
    g.item(1;9) = g.public.project
    g.item(10;38) = g.public.material

    return (0)
}

function long public.material.map.from.item()
{
    g.public.material = g.item(10;38)
    return (0)
}
```

## Error Handling
In the development part, it is possible to report problems. The standard function 'dal.set.error.message' have to be used for setting an error message, followed by 'return (DALHOOKERROR)'.

## Related topics
- [Business Object Layer](overview.md)
- [Public Layer](sb_layer.md)
- [Protected Layer](st_layer.md)
- [Interface Conversion Protected Layer](sm_layer.md)
- [Specific Methods Library](sf_layer.md)
