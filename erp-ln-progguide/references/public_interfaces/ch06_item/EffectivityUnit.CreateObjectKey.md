# EffectivityUnit.CreateObjectKey

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for EffectivityUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 242-244

```baan
DLL:   tcextuefapi
This function is available from     2026.02 (KB3643749  ).
Syntax: long EffectivityUnit.CreateObjectKey(
domain  tctabl.c         iTable,
ref     domain  tcuef.obje       oCompressedKey,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Create a compressed object key based on the input table and its
Primary index field.
Note: this function uses variable arguments, for input.
Data is retrieved via values: specify the primary key values.
Example: when compressed object key is needed, the function must
be called as follows:
if EffectivityUnit.CreateObjectKey(
|* Fixed arguments:
tibom310,                                                            --   > input
CompressedKey                                                           --> output
oExceptionMessage,                                                      --> output
oExceptionID,                                                           --> output
|* Variable arguments:
"SITE01",                                                            --   > input
"         900                                              -660",       --> input
"STDBOM",                                                            --   > input
"000001",                                                            --   > input
"60") <> 0 then                                                         --> input
|* Error, do something
Exception.Delete(exception.id)
endif
Pre:    None
Post:   None
Input:
iTable                                        - Table to which the unit applies.
...                                           - Variable arguments: Primary key field values
Output:
oCompressedKey                                - Compressed Key
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Compressed key created successfully.
<> 0                                          - Otherwise.
```

## Public Interfaces for SerializedItem

The following functions are available: SerializedItem.StartDetail SerializedItem.StartOverview
