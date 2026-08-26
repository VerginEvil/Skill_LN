# Include files (preprocessor)
To include files, use one of the following statements:
```

#include "filename"
#include <filename>
```
Files included between '<' and '>' are searched for in the directory '$BSE/include<rel.number>'. This directory is reserved for system headers and cannot be used for applications. Normally a file specified between quotes is searched for using the standard file redirection method.
Note that the preprocessor works only during compilation of a 3GL source, as the standard generator std_gen6.2 does not have a preprocessor pass. So it is not possible to use 4GL events in an included file.

## Example
Suppose the following entry occurs in $BSE/lib/fd.6.2<package_comb>:
```

ippmmm:/usr/bse/standard6.2
```
and there is an include statement as follows:
```

#include "ippmmmheader"
```
The file "/usr/bse/standard6.21/ippmmm/immmheader0" is included. If a '/' occurs in the filename, the file is searched using the specified path name. When a file is included twice, the second include is ignored.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
