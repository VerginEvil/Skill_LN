# Protected Layer
Methods in this library are used to actually perform tasks on Components.
Components hide the implementation of the persistency layer. The Protected Layer can be regarded as the successor of the socalled 'Integration Library'. Standard methods, like 'Create', 'Change', 'Delete', etc. will call DAL2 methods or Sessions (via the Function Server). The execution logic of the methods List and Show are also part of this layer.
The Protected Layer is generated completely by the system, thefore the script is read-only.
Within the Protected Layer so-called setter and getter functions are present. These functions have to be used to send and retrieve data in other layers. Also in the Protected Layer functions are present is retrieve information whether an attribute has been set before.
'Getter' functions looks like:
- <dll name>.get.<component name>.<attribute>()
- example: gaadv.bl090st00.get.Header.payByBP()
- example without component: gaadv.bl091st00.get.payByBP()   'Setter' functions looks like:
- <dll name>.set.<component name>.<attribute>(value)
- example: gaadv.bl090st00.set.Header.customerReference(value)
- example without component: gaadv.bl091st00.set.payByBP(value)   Functions to detect whether an attribute have been set looks like:
- <dll name>.is.set.<component name>.<attribute>()
- example: gaadv.bl090st00.is.set.Header.payByBP()
- example without component: gaadv.bl091st00.is.set.payByBP()   Also within the Protected Layer a function is present to get the result of a method.
- <dll name>.get.method.result()
- example: gaadv.bl090st00.get.method.result()

## Related topics
- [Business Object Layer](overview.md)
- [Public Layer](sb_layer.md)
- [Interface Conversion Public Layer](sc_layer.md)
- [Interface Conversion Protected Layer](sm_layer.md)
- [Specific Methods Library](sf_layer.md)
