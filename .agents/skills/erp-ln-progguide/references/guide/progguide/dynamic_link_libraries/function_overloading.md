# Function overloading
When DLLs are dynamically linked at runtime, instead of at compile time, function overloading is possible. This means that an external function contained in a loaded DLL can be replaced by overloading another DLL that contains a function with the same name and arguments.
You use the [load_dll()](../functions_dll/load_dll.md) function to load DLLs dynamically. When you call this function, you can specify whether the DLL is to be overloaded or not. When searching for an external function called by a program, the bshell always searches in overloaded DLLs first.

## Specifying which DLLs belong to an object
There are three methods for specifying which DLLs belong to an object.

- Specify the DLL dynamically, with overload, in the source code. For example: `load_dll( <dll_object>, DLL_OVERLOAD )`

- use the option "Define Libraries" in the session "Maintain Program Scripts"

- use the following syntax when starting the bic6.2 compiler `bic6.2 script -o object -d dll_object`

- use the following pragma code in the script `#pragma used dll <dll_object>`

- Specify the DLL dynamically, without overload, in the source code. For example:
```

load_dll( <dll_object>, 0 ) or
load_dll( <dll_object> )    | 0 is default
```

## Function search algorithm
When a DLL function is called for the first time, the function address is unresolved. The bshell attempts to resolve the function address by searching for the function using the search method described below. After a function address is resolved, that address is used for all subsequent function calls with the same function name and arguments. So once a function address is resolved, the function cannot be replaced by overloading a different DLL containing a function of the same name and arguments.
The bshell searches DLLs in the following order:

- All dynamically overloaded DLLs, that is: DLLs loaded by calling [load_dll()](../functions_dll/load_dll.md) with the overload flag set to DLL_OVERLOAD. For example: `load_dll(dll_object, DLL_OVERLOAD)` The bshell searches the overloaded DLLs in reverse order. So, the DLL that was overloaded last is searched first.

- The first DLL where the function was found during compilation.

- All statically specified DLLs.

- First the bshell searches in the DLLs specified in the compilation command with the -d option. The DLLs are searched in the order they are specified in the command. For example: `bic6.2 script -o object -d odll1:odll2:odll3` Next the bshell searches in DLLs specified using the following pragma statement: `#pragma used dll <dll_object>`

- 4 All dynamically loaded DLLs, that is: DLLs loaded by calling [load_dll()](../functions_dll/load_dll.md) without the overload flag or with the overload flag set to 0. For example: `load_dll(dll_object, 0` The bshell searches the loaded DLLs in the order in which they were loaded. So, the DLL that was loaded first is searched first.Note that you can change the search order of dynamically loaded DLLs by calling *load.dll()* for a loaded DLL and changing the value of the overload flag.

## Function overloading example
```

Compile

bic6.2 dll -o odll
bic6.2 dll_new -o odll_new
bic6.2 script -o object -d odll -DDEBUG

Script code

function main()
{
#ifdef DEBUG
        if ( debug flag ) then
                | Load dynamically DLL 'dll_new' to
                | overload the DLL 'dll'
                load_dll("odll_new", 1) | Argument '1' means overload
        endif
#endif
        dll_function()
}

dll code

function extern dll_function()
{
        ...
}

dll_new code

function extern dll_function()
{
        ...
}
```

## Related topics
- [Dynamic-link libraries](overview.md)
