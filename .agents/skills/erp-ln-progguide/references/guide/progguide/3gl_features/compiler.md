# Compiler
You compile program scripts with the bic6.2 compiler. The compiler is automatically activated after you have edited your program or report script and after the use of std_gen6.2 and repgen6.2 at the option 'Compile' in the data dictionary. You can also use the compiler to compile 3GL programs
The syntax for the compiler is:
```

bic6.2 [-ilptz67sV] [-wW[level]] [-WA] [-Xx[level]] [-o <object>] [-d dll[:dll...]]
       [-D <macro>] [-I <dir>] [-T <TIV>] source
```
| | |
|---|---|
| `-i` | Assembler output is stored in <source>.i. Do not specify an object file. |
| `-l` | Object will run in debug mode. |
| `-p` | Object will run in profiling mode for time analysis (see function times.on()). |
| `-t` | Print tokens after preprocessor pass. |
| `-pacc pack_comb` | Use specified package combination. |
| `-u[l]` | Create 'where used' list [ for level l]. |
| `-f fn` | File name for 'where used' output file. |
| `-z` | Ignore the BAAN_SCM_GRP variable for VRC searches. |
| `-6` | Generate 6.1 object format. |
| `-7` | Generate 7.2 object format. This is the default. |
| `-s` | Generate symbol table to stdout; for more information use 'bic_info6.2 -s'. |
| `-V` | Print release information. |
| `-w` | Suppress all warnings. Warnings explicitly enabled by the -W or -Wn command line option are not suppressed. |
| `-wn` | Suppress warnings of level n, unless explicitly enabled by the -W or -Wn command line option. Some warnings are suppressed by default. |
| `-W` | Give warnings of all levels, even if implicitly suppressed by default or explicitly suppressed by the -w or -wn command line option. |
| `-Wn` | Give warnings of level n, even if implicitly suppressed by default or explicitly suppressed by the -w or -wn command line option. Most warnings are enabled by default. Others must be explicitly switched on. |
| `-WA` | Do not suppress warnings after first error. By default, after the first error all further warnings are suppressed, except those warnings that are considered as errors. |
| `-X` | Consider warnings of all levels as errors, except those warnings for which this behavior is explicitly switched off by means of the -x or -xn command line option. Warnings that are suppressed, remain suppressed. This command line option is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md) |
| `-Xn` | Warnings of level n are considered as errors, except when that is explicitly switched off by means of the -x or -xn command line option. Further, this command line option implies the behavior or the -Wn command line option, i.e. warnings of level n are switched on, even if implicitly suppressed by default or explicitly suppressed by the -w or -wn command line option. This command line option is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md) |
| `-x` | Do not consider any warning as an error, even if the -X or -Xn command line option says so. This command line option is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md) |
| `-xn` | Do not consider warnings of level n as errors, even if the -X or -Xn command line option says so. This command line option is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md) |
| `-o <obj>` | Specifies the object name; when not specified, only a syntax check is performed. |
| `-d` | Specifies the DLL(s), separated by a colon (':'). These are the objects of dynamic-link libraries necessary to compile the source program. |
| `-D<macro>` | Specifies a condition <macro>, see also [Preprocessor](preprocessor.md). |
| `-I<dir>` | Specifies the directories (separated by a colon (':')) where include files are located. |
| `-T <TIV>` | Specifies the [TIV](../tiv/tiv_overview.md) number to be assigned to the object. At runtime, this value is available in the object as the result of the expression [GET.OBJECT.TIV()](../tiv/tiv_overview.md) and it can be retrieved for any object by means of the expression [GET.OBJECT.TIV(object.name)](../tiv/tiv_overview.md), where *object.name* is a string expression specifying the name of the object. Typically, the value supplied here is the TIV number as specified in session "Program Scripts / Libraries (ttadv2530m000)". |
The warnings associated with the various level numbers are as follows:
```

dummy = ittadv0037.search.label(....)
```
```

long a
long b
a = 1
b = 3
a / b = 0 and not 0.33
```
```

function test.a()
{
    if a = 0 then
        ...
        return()
    else
        ...
        return()
    endif
    a = 1
}
```
```

function double d()

function main()
{
    domain tttst.db62   dbldom
    double              a, b

    if a = b then
        ...
    endif
    if d() > a then
        ...
    endif
    if a <= dbldom then
        ...
    endif
}
```
```

extern long a

function main()
{
    a = 5
    make.ten(a)
    message("a = %d", a)   | results in a = 10
}

function make.ten( ref long x )
{
    message("a = %d", a)   | results in a = 5
    x = 10
    ....
    message("a = %d", a)   | results in a = 5
}
```
```

string a(20)   fixed
function process.variable( ref string b )
{
}
```
```

function test()
{
    extern long a
    ....
}
```
```

function test()
{
    long    l
    boolean b
    l = b
    l = (a > 10)
}
```
```

function test()
{
    long    l
    boolean b
    b = l
    b = 0
}
```
| | |
|---|---|
| Level | Warning |
| 1 | Declared but never used For example, remove the declaration of the non-used variables. Warnings related to an include file can be prevented by entering [#pragma nowarnings](pragma_codes_preprocessor.md) at the beginning of the include file. All warnings caused by the include file will then be ignored. |
| 2 | Function never used A function is found but never called. For instance remove the function. This warning related to an include file can be prevented by entering [#pragma nowarnings](pragma_codes_preprocessor.md). |
| 3 | Return value of function ignored When a function yields a value, that value must be checked. The reason is that many functions return TRUE or FALSE, depending on whether the action has been completed successfully or not. If the return value is of no importance, a dummy value must be assigned to the function. For example: |
| 4 | A long divided by a long gives also a long A long divided by a long will result in a long. For example: |
| 5 | Statement/Label not reached Occurs if a statement cannot be reached. For example: The statement a = 1 will never be reached, so this warning indicates a programming error or logical error. |
| 6 | Comparison of two float types may yield unpredictable results This warning is given when two double types are compared for equivalence. Please use the function [double.cmp()](../functions_mathematical_operations/double.cmp.md) to compare double variables, double domains, and double functions. Note that for double functions the warning appears only if the function has been prototyped before its actual use. For example: All the above expressions may yield unpredictable results, as no tolerances have been specified. |
| 8 | Due to compatibility reasons, function [at.base( long process_id, const string basic_variable_name,... )](../functions_variables_based/at.base2.md) skips the third argument. This warning is suppressed by default. Use compiler option -W8 to switch it on. |
| 9 | External variable '%s' passed as reference to function '%s' When an external variable is given as a call by reference to a function, the value of this variable within the function is not equal to the local value. Just after the return, the value of the external variable will be changed. For example: When within the function make.ten() another function is called using the external variable a, the variable a still has the value 5. |
| 10 | Passing fixed variable to non-fixed call by reference argument (or non-fixed to fixed) When a global variable is declared as fixed, the variable within a function is still regarded as fixed, although the reference declaration is not fixed. For example: If the function is invoked using the argument "a", "b" is considered fixed. |
| 12 | External variable '%s' added in external symbol table An external variable is declared within a function. For example: |
| 13 | System library <bic_stdlib> NOT included ! |
| 15 | Warning given by #pragma <text> This is a warning of your own format, see [Pragma codes (preprocessor)](pragma_codes_preprocessor.md). |
| 16 | Missing selectdo; automatic break or Missing selectdo; loop until selecteos When a selectdo is missing in the select statement, an automatic break is generated to prevent unnecessary use of cpu time. When a selectdo is missing, while a selecteos section exists, the select statement should be executed. Probably this is a non optimal select statement. |
| 18 | Macro '%s' redefined The named macro, which was already defined with the same arguments, is defined again. |
| 19 | Function '%s' in DLL '%s' ignored taken from '%s' A duplicate function occurs in a DLL or program script. A function is searched for in the script first and next in the libraries that are linked to the script in the specified order. If a function is found twice, this warning appears. |
| 23 | (Subscripted) variable <variable name> is used as single argument of function <one of [set.fmax()](../functions_mathematical_operations/set.fmax.md), [set.fmin()](../functions_mathematical_operations/set.fmin.md), [set.max()](../functions_mathematical_operations/set.max.md), [set.min()](../functions_mathematical_operations/set.min.md) >, but at runtime it is not known that the compile time type of this variable is domain <domain name> (base type <type name>). At runtime, type <type name> will be used, with <minimum or maximum> value <value>, instead of <minimum or maximum> value <value> of domain <domain name>. Please explicitly specify the domain to be used, e.g. domainof(<variable name>), and supply it as the second argument to function <one of [set.fmax()](../functions_mathematical_operations/set.fmax.md), [set.fmin()](../functions_mathematical_operations/set.fmin.md), [set.max()](../functions_mathematical_operations/set.max.md), [set.min()](../functions_mathematical_operations/set.min.md) >. |
| 24 | Explicitly declared variable <variable name> is used as single unsubscripted argument of function <one of [set.fmax()](../functions_mathematical_operations/set.fmax.md), [set.fmin()](../functions_mathematical_operations/set.fmin.md), [set.max()](../functions_mathematical_operations/set.max.md), [set.min()](../functions_mathematical_operations/set.min.md) >, but its runtime name <runtime variable name> <may match or matches> a table field. |
| 25 | Simulating built in Boolean data type. Reserved keyword boolean, true or false is defined as long, 1 or 0. |
| 26 | Macro '%s' has illegal body (future keyword). Reserved keyword boolean, true or false is defined as another value as long, 1 or 0. |
| 27 | Casting boolean to numeric not allowed. For example:This warning is suppressed by default. Use compiler option -W27 to switch it on. |
| 28 | Casting numeric to boolean not allowed. For example:This warning is suppressed by default. Use compiler option -W28 to switch it on. |
| 29 | Future error. Used for several different cases of incorrect use of the 3GL language. Due to compatibility reasons, such incorrect use is allowed in existing code, but even then it is preferred that the 3GL code is repaired. For each separate case, as of a certain [TIV level](../tiv/tiv_overview.md), the warning will become an error. |
| 31 | Duplicate value in case (ignored) |
| 32 | [Constant integer expression](arithmetic_operators.md#compile_time_constants) outside signed 32-bit range. This warning is suppressed by default. Use compiler option -W32 to switch it on. As of [porting set TIV](../tiv/tiv_overview.md) [level 2030](../tiv/tiv_2030.md), warnings triggered by this compiler option are not suppressed by [#pragma nowarnings](pragma_codes_preprocessor.md). |
You can specify the options for automatic compilation in the session Development Parameters Template (ttams1150m000).
When an error is found in the program, all warnings after that error are suppressed.

## Related topics
- [3GL programming language features: overview](overview.md)
