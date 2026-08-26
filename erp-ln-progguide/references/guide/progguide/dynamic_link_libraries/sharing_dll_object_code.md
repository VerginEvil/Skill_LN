# Sharing DLL object code
DLL objects contain both a program code part and a data part. The program code of a DLL object is loaded into memory when one of the DLL's functions is called. The data part defines the memory part available for variables. Memory is allocated for a variable the first time that variable is used.
The program code part of a DLL can be loaded into a common virtual memory address space. This enables two or more sessions, within one or more bshells on the same system, to share the program code. The data part is not loaded into shared memory and so cannot be shared.
By default, the program code of Infor Enterprise Server DLLs can be shared only within the same bshell. Once the DLL has been loaded, it is shared by all process within the bshell.
For process within all bshells on the same system to be able to share the program code, you must specify the object name in the file $BSE/lib/srdd_tab6.2. The object will be loaded automatically and its code will be shared by sessions within all bshells on the same system. It is advisable to use this method for all DLLs that are frequently used by several users. For more details, consult the Shared memory manager section in the Infor Enterprise Server Technical Manual.

## Related topics
- [Dynamic-link libraries](overview.md)
