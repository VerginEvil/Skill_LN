# Dynamic linking
DLLs can be linked to a program script either at compile time or at runtime.

## Dynamic linking at compile time
For dynamic linking at compile time, you must specify the libraries that belong to a program script when you create or update that script. Which libraries belong to a program script depends on which external functions the program uses. It is necessary to specify the libraries at compile time because the compiler locates the functions and checks the types of arguments and return values with the function prototypes. Note that a DLL object is loaded into memory and linked to the executable program at runtime, at the time a DLL function is called.
You must compile the libraries before you compile the program script that uses those libraries. However, since loading and linking take place at runtime, when a library is changed, you need only compile the library and restart the program.
The are two ways to compile the libraries and program script:

- Use the Infor Enterprise Server. Choose the Compile option in the sessions "Maintain Libraries" and "Maintain Program Scripts".

- Use the bic6.2 compiler. For example: `$ bic6.2 dll1 -o odll1 $ bic6.2 dll2 -o odll2 $ bic6.2 dll3 -o odll3 $ bic6.2 <program> -o<object> -d odll1:odll2:odll3`

Note that, at runtime, external functions are searched for in the order in which the DLLs were supplied during compilation. In above example, dll1 is first.

## Dynamic linking at runtime
This is used in cases where the DLL(s) that must be linked to a program are known only at runtime.
For example, consider a programmer's interface that receives a string containing the library or external function to be called. The return value of the function call (if any) is sent back to the calling process. In this case dynamic linking at runtime must be used, because only at runtime is it known which external function must be called.
A number of functions are available for handling dynamic linking at runtime. Using these functions, you can load a specific DLL and execute one or more of its functions. See [DLL functions (executing) overview and synopsis](../functions_dll/overview_and_synopsis.md).

## Related topics
- [Dynamic-link libraries](overview.md)
