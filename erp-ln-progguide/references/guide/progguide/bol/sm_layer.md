# Interface Conversion Protected Layer
In this library the logic of the protected calculated fields must be programmed in specific hooks:
- function long <component>.{all|<attribute>}.map.to.{specific|<attribute>}()
- function long <component>.<attribute>.map.from.{all|specific|<attribute>}()   'all' will be used when more then one attribute has been mapped to the current attribute. Normally the mapped attribute will be filled out in <attribute>. If there is no mapping specified 'specific' will be used instead.
The system will generate the library. The file can be divided into two parts. The first part is read-only, while in the second part the content of the hooks must be programmed (see the example below).

## Example Read-only
```

function extern long
tlbct.bl750sm00.set.Line.localPriceIncludingVAT(
                    const domain tlpro.amnt i.value)
{
    DllUsage
    EndDllUsage

    g.Line.localPriceIncludingVAT = i.value
    g.Line.localPriceIncludingVAT.set = true

    RETIFNOK(Line.localPriceIncludingVAT.map.to.specific())
    return(0)
}

function extern long
tlbct.bl750sm00.get.Line.localUnitPriceIncludingTaxAmount(
                    ref domain tlpro.prip o.value)
{
    DllUsage
    EndDllUsage

    CALL_PROT_DYN("get.Line.localUnitPriceOfAmount",
            g.Line.localUnitPriceOfAmount)
    g.Line.localUnitPriceOfAmount.set = true
    CALL_PROT_DYN("get.Line.taxAmount",
            g.Line.taxAmount)
    g.Line.taxAmount.set = true
    RETIFNOK(Line.localUnitPriceIncludingTaxAmount.map.from.all())
    o.value = g.Line.localUnitPriceIncludingTaxAmount
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

function long Line.localPriceIncludingVAT.map.to.specific()
{
    return (0)
}

function long Line.localUnitPriceIncludingTaxAmount.map.from.all()
{
    g.Line.localUnitPriceIncludingTaxAmount =
g.Line.localUnitPriceOfAmount
        + g.Line.taxAmount
    return (0)
}
```

## Error Handling
In the development part, it is possible to report problems. The standard function 'dal.set.error.message' have to be used for setting an error message, followed by 'return (DALHOOKERROR)'.

## Related topics
- [Business Object Layer](overview.md)
- [Public Layer](sb_layer.md)
- [Interface Conversion Public Layer](sc_layer.md)
- [Protected Layer](st_layer.md)
- [Specific Methods Library](sf_layer.md)
