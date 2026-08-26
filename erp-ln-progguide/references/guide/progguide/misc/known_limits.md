# Known limits

## Reports
- sorting doubles correct to 6 decimal places
- Report TIV < 1101: maximum of 255 fields on a report (including array elements)
- Report TIV >= 1101: maximum of 512 fields on a report (including array elements)

## Bshell
- maximum function stack depth is 500

## Bic
- maximum 255 arguments per function
- maximum 32K variables per compilation
- maximum BRANCH of 32K (BRANCH refers to the amount of generated code per function, including macros etc.)

## SQL
- The nesting level of subqueries is limited to 10. The nesting level is defined as follows. The nesting level of the main query is 1. The nesting level of a sub query immediately contained in the main query is 2. The nesting level of a sub query immediately contained in another sub query is the nesting level of that sub query plus 1.
- The number of index hints that can be given on a table is limited to 4.
- The SQL processor has no limit on the length of string values. However, the databases may impose restrictions on the length of string values. It is advised to keep the length of string values (including string literals and string values resulting from concatenation) below 4K.

## Tables
- maximum record length is 3072 bytes (for multibyte columns take a factor 2 into account. For example, a multibyte string of 256 characters will be 512 bytes long in a multibyte environment.)
- maximum number of fields is 1024
- maximum field length is 3072 bytes
- maximum number of indices per table is 20

## Indexes
- maximum index length is 500 bytes
- maximum number of fields is 16 (each individual field in a combined field counts as 1). This limit is not enforced by the porting set, but should be obeyed when developing standard software. The limit is raised by Microsoft SQL Server.
