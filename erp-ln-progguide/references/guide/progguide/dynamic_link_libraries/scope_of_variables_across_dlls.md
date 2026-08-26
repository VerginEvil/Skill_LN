# Scope of variables across DLLs

## Global variables
Global variables are declared outside the functions in a script, without the EXTERN keyword. They are only known within the DLL in which they are declared. For example:
`long var_1`

## External variables
External variables are declared outside the functions in a script, with the EXTERN keyword. They are known within all DLLs in the process in which they are declared. For example:
`extern long var_2`

## Database fields
Database tables are declared as follows:
`table t<table_name>`
Declaration of a table implies declaration of all its fields also. Though a table declaration does not include the EXTERN keyword, tables fields are known within all DLLs in the process in which they are declared. When one DLL in a process reads a record, the values of the record fields are shared by all DLLs in the same process.

## Related topics
- [Dynamic-link libraries](overview.md)
