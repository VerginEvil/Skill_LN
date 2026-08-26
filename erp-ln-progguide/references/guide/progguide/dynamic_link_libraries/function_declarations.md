# Function declarations
For functions programmed within a DLL to be accessible to other programs, they must be declared as external functions, that is, they must be declared with the keyword EXTERN. For example:
```

function extern long funct_a( long arg )
{
.....
}
```
Functions declared without the EXTERN keyword are local functions. They are accessible only within the program in which they are declared. A DLL usually contains both local and external functions.

## Managed Execution
Normally it will not be allowed for a function in a trusted dll, to be called from a not trusted object. Using the '@trusted' keyword will allow a function to be called from any object. More about trusted and not trusted objects can be found in the section about [managed execution](../misc/managed_execution.md).
```

function extern long funct_a( long arg ) @trusted
{
.....
}
```
The '@trusted' keyword can only be used in combination with the 'extern' keyword and is available from TIV level 2000.

## Related topics
- [Dynamic-link libraries](overview.md)
- [Managed Execution](../misc/managed_execution.md)
