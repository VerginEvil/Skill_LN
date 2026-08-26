# bpext.xtm0001.define.processing.instructions

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ExtendedTimeManagement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2009-2010

```baan
Syntax: long bpext.xtm0001.define.processing.instructions(
ref             long             o.number.of.elements,
ref     domain  bpxtm.proc.ins   o.processing.instructions() fixed )
Usage:        Expl:
Use this method to define an extra list of names for processing
instructions which can be called.
This list will be shown in the session Processing Instructions
(bpxtm0160m000) in the field Instruction (bpxtm060.funa).
Instruction can be executed during Generate Actual Attendance
for every day and every employee which is under review based on
settings in table Processing Instructions (bpxtm060) using
function bpext.xtm0001.execute.processing.instruction().
----------------------------------------------------------------
Start of Example of Implementation
long    domain.length.bpxtm.proc.ins
long    dummy.convert
rdi.domain.string(      "bpxtm.proc.ins",
domain.length.bpxtm.proc.ins,   |* ref
dummy.convert)                  |* ref
o.number.of.elements = 4        |* 4 processing instructions
|* will be defined and returned
if (alloc.mem(  o.processing.instructions,
domain.length.bpxtm.proc.ins,
o.number.of.elements) <> 0 ) then
return(DALHOOKERROR)
endif
o.processing.instructions(1,1) = "instr_0001"
o.processing.instructions(1,2) = "instr_0002"
o.processing.instructions(1,3) = "instr_0003"
o.processing.instructions(1,4) = "instr_0004"
return (0)
End of Example of Implementation
----------------------------------------------------------------
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.number.of.elements                  - Number of processing instructions
o.processing.instructions
-                                               Array with instruction names
Return: 0                                     - Success
<> 0                                          - When an error occurs in setting
processing instructions.
```
