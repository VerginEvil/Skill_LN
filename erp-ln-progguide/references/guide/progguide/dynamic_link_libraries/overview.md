# Dynamic-link libraries
Infor Enterprise Server supports the use of dynamic-link libraries (DLLs). A DLL consists of a library of functions that are compiled, linked, and stored separately from the processes that use them. The functions are resources that can be shared by multiple programs that are running concurrently. Only one copy of the DLL needs to be present in memory. Each program that uses the DLL links to it at runtime, at the time it calls one of the DLL's functions.
For example, consider the *sprintf$()* function. This is a very common function, used by many programs. Instead of including a copy of the function in each program that uses it, you can program the function in a separate DLL. Multiple programs can then share this one copy of the function, by linking to the DLL at runtime.
The following are some of the benefits of using DLLs:
- Instead of programming common functions in each program that uses them, you can program the functions in one or more DLLs. The code can then be shared by all the programs that use it. By implementing DLLs in Infor Enterprise Server applications, you can reduce the size of objects to a minimum, as the 4GL engine is not merged with each 4GL program script.
- You can upgrade a function within a DLL without recompiling all the applications that use it.
- You can upgrade an application without recompiling all the DLLs it uses.
- A DLL is loaded only when required. It is also loaded only once, though multiple programs can share its code.   The following sections describe how you handle DLLs:
- [Function declarations](function_declarations.md)
- [Scope of variables across DLLs](scope_of_variables_across_dlls.md)
- [Sharing DLL object code](sharing_dll_object_code.md)
- [Dynamic linking](dynamic_linking.md)
- [Function overloading](function_overloading.md)
- [Object information tool](object_information_tool.md)
- [DLL compilation and runtime errors](dll_compilation_and_runtime_errors.md)
