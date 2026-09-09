# bpext.xtm0001.execute.processing.instruction

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ExtendedTimeManagement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2029-2029

```baan
Syntax: long bpext.xtm0001.execute.processing.instruction(
domain  bpxtm.proc.ins   i.processing.instruction )
Usage:        Expl:
Use this method to execute a processing instruction based on
its name.
Instruction can be executed during Generate Actual Attendance
for every day and every emplyee which is under review based on
settings in table Processing Instructions (bpxtm060).
This can be used to define a mapping between processing
instruction names and real function names.
----------------------------------------------------------------
Start of Example of Implementation
on case trim$(i.processing.instruction)
case "instr_0001":
my.proc_0001()
break
case "instr_0002":
my.proc_0002()
break
case "instr_0003":
my.proc_0003()
break
case "instr_0004":
my.proc_0004()
break
default:
return(DALHOOKERROR)
endcase
return (0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  i.processing.instruction
- Instruction name
Output: N.A.
Return: 0                       - Success
<> 0                    - When an error occurs in executing
a processing instruction.
```
