# ProductVariant.AddCustomCPQIntegrationParameters

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2168-2169

```baan
Add Custom CPQ Integration Parameters to configuration request.
This process extension is available from 2024.03 (KB2291878).
Technical information for this process extension:
Usage:                This process extension is called during construction of the configuration
request for CPQ. In addition to the standard CPQ Integration Parameters,
custom integration parameters may be added to the request structure.
The extension provides hooks for:
- Registration of the additional CPQ integration parameters
(method tiext.pcf0003.register.cpq.integration.parameters).
- Retrieval of a value of a registered additional CPQ integration
parameter (method tiext.pcf0003.get.cpq.integration.parameter.value).
To implement this process extension, you need to implement the following method(s):
```
