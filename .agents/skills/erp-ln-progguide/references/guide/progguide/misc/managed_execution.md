# Managed Execution

## Trusting object files
In a traditional installation all sessions essentially run under the same authorization. This changes drastically in e.g. a multi-tenant environment, where the landlord has a very different authorization compared to the tenants. Tenants may under no circumstance be able to execute a session which might influence another tenant.
Therefore a differentiation is made between trusted and non-trusted object files. A trusted object file may still do everything, just like in a traditional installation. A non-trusted object, however, is limited in the functions it may execute. Some bshell functions are not allowed in non-trusted objects (such as 'shell'), nor are calls to functions in trusted objects allowed (unless these are explicitly allowed by adding the '@trusted' keyword). Typical examples of trusted objects are the applications as provided by Infor. Typical examples of non-trusted objects are objects compiled by the user, based upon user generated sources, such as reports.
```
tools
application
```
