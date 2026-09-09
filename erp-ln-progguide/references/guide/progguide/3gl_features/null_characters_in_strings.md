# NULL characters in strings
A string is a sequence of characters. A string variable may contain a NULL character (also named null or abbreviated to [NUL](../misc/ascii_table.md)). The NULL character is encoded by means of a byte with the value 0 (zero).
Usually, such a NULL character is interpreted as an end of string marker. According to that interpretation, the NULL character itself is not part of the string value. Also all the bytes after the NULL character, until the end of the memory available for the string, are not part of the string value and their content is in most cases irrelevant.
This way, the [character length](data_types.md#character length) of the string value stored in a string variable may be smaller than the [character capacity](data_types.md#character capacity) of the string variable.
Likewise, the [byte length](data_types.md#byte length) of the string value stored in a string variable may be smaller than the [byte capacity](data_types.md#byte capacity) of the string variable.
As an example, the following piece of code shows the assignment of string values of different lengths to a string variable of length 6.
```

STRING	my_string(6)

my_string = "abcdef"    | String variable my_string now contains string value "abcdef".
                        | The string variable my_string is completely filled.

my_string = "abcde"     | String variable my_string now contains string value "abcde".
                        | The sixth character in my_string is a NULL character.

my_string = "abcd"      | String variable my_string now contains string value "abcd".
                        | The fifth character in my_string is a NULL character.
                        | Any further data in my_string is irrelevant.

my_string = ""          | String variable my_string now contains the empty string value "".
                        | The first character in my_string is a NULL character.
                        | Any further data in my_string is irrelevant.
```

## Zero-padding
As said above, in most cases the value of the bytes after the terminating NULL character is irrelevant. When an explicit action is performed in order to observe the value of any of these bytes, then it becomes relevant what their value is. It is the intention to let such bytes be observed as if *zero-padding* had taken place, i.e. as if all bytes after the terminating NULL character have the value 0.
However, zero-padding is a too expensive action to be performed immediately whenever applicable, e.g. as part of each assignment of a string value to a variable with a higher [byte capacity](data_types.md#byte capacity) than the [byte length](data_types.md#byte length) of the assigned string value.
Therefore, instead of performing the actual zero-padding, the string variable is marked *dirty*. This indicates that the bytes after the terminating NULL character have an undefined value, but should be considered as having the value 0.
Whenever any action is performed to observe the actual value of a possibly dirty byte, first the actual zero-padding is performed and the *dirty* mark is removed from the string variable.
The following example shows how this can be observed in the debugger.
```

STRING	my_string(4)

my_string = "abcd"
```
Variable my_string now contains string value "abcd" and is completely filled.
```

LONG	my_long

my_long   = load.long( my_string )
```
Variable my_long now contains the value 1633837924. In hexadecimal notation this is the value 0x61626364, i.e. the ASCII codes for the characters 'a', 'b', 'c', and 'd' respectively.
```

my_string = "ab"
```
Variable my_string now contains string value "ab". The third character in my_string is a NULL character. Any further data in my_string is irrelevant. However, in the debugger this can be observed. The [debugger command](../debugger/debugger_commands.md) `my_string/d` shows that my_string is marked dirty:
```

flags: (STRING|DIRTY|NO_ALLOC_MEM)
```
The [debugger command](../debugger/debugger_commands.md) `my_string/X` shows that after the NULL character there is still the character 'd':
```

my_string = "ab\0x00d"
```
Now we trigger the actual zero-padding:
```

my_long   = load.long( my_string )
```
Variable my_long now contains the value 1633812480. In hexadecimal notation this is the value 0x61620000, i.e. zero-padding was done. The [debugger commands](../debugger/debugger_commands.md) `my_string/d` and `my_string/X` show that my_string is no longer marked dirty and that zero-padding was done:
```

flags: (STRING|NO_ALLOC_MEM)
my_string = "ab\0x00\0x00"
```
Repeat the scenario with a different way of triggering the actual zero-padding
```

my_string = "abcd"
my_string = "ab"
```
Variable my_string is marked dirty. The [debugger commands](../debugger/debugger_commands.md) `my_string/d` and `my_string/X` show that my_string is marked dirty and not yet zero-padded:
```

flags: (STRING|DIRTY|NO_ALLOC_MEM)
my_string = "ab\0x00d"
```
Now we trigger the actual zero-padding:
```

STRING	my_character(1)

my_character   = my_string(4)
```
Variable my_character now contains the empty string, i.e. zero-padding of my_string was done before accessing it with index 4. The [debugger commands](../debugger/debugger_commands.md) `my_string/d` and `my_string/X` show that my_string is no longer marked dirty and that zero-padding was done:
```

flags: (STRING|NO_ALLOC_MEM)
my_string = "ab\0x00\0x00"
```

## Binary strings
As said, the usual interpretation of a NULL character is that it marks the end of a string value, making the value of subsequent bytes irrelevant. However, there are circumstances where the bytes after the NULL character are certainly relevant. Generally spoken, that is the case when a string value is considered as a ‘sequence of bytes’, without the intention to interpret it as a NULL-terminated sequence of TSS-encoded characters. For such string values we use the term *binary string*. Special attention is needed to modify and to observe such string values.

## Modifying a binary string
There are several ways to modify the value of separate bytes of a string variable without interpreting them as a NULL-terminated sequence of TSS-encoded characters. The following list shows several examples.

- [seq.read()](../functions_directory_file_operations/seq.read.md). The bytes read from the specified file are stored into the specified buffer, without any interpretation.

- [store.byte()](../functions_string_operations/store.byte.md), [store.short()](../functions_string_operations/store.short.md), [store.long()](../functions_string_operations/store.long.md), [store.double()](../functions_string_operations/store.double.md), [store.float()](../functions_string_operations/store.float.md), [store.utc()](../functions_string_operations/store.utc.md). These functions treat the ref string supplied as their second argument merely as a sequence of bytes. The bytes written to the string are not the encoding of certain characters, but the applicable encoding of the first argument of each function.

- [copy.mem()](../functions_memory_operations/copy.mem.md). The number of bytes to be copied is determined by the properties of the source and destination arguments (type and declared capacity, etc.), *not* by their current value. The copied bytes are not interpreted.

- [base64.decode()](../functions_base64/base64.decode.md). The binary output resulting from the decoding of the base64-encoded input is stored in the output string, without any interpretation. Any subsequent bytes of the output string are left unchanged.

- [base64.encode()](../functions_base64/base64.encode.md). The base64-encoded output resulting from the encoding of the binary input is stored in the output string, *without* NULL-termination. Any subsequent bytes of the output string are left unchanged.

## Observing a binary string
There are several ways to observe the value of separate bytes of a string variable without interpreting them as a NULL-terminated sequence of TSS-encoded characters. The following list shows several examples.

- [seq.write()](../functions_directory_file_operations/seq.write.md). The specified number of bytes from the specified buffer are written to the specified file, without any interpretation.

- [load.byte()](../functions_string_operations/load.byte.md), [load.short()](../functions_string_operations/load.short.md), [load.long()](../functions_string_operations/load.long.md), [load.double()](../functions_string_operations/load.double.md), [load.float()](../functions_string_operations/load.float.md), [load.utc()](../functions_string_operations/load.utc.md). These functions treat the string supplied as their argument merely as a sequence of bytes. The bytes read from the string are not the encoding of certain characters, but the applicable encoding of the value to be returned by each function.

- [copy.mem()](../functions_memory_operations/copy.mem.md). The number of bytes to be copied is determined by the properties of the source and destination arguments (type and declared capacity, etc.), *not* by their current value. The copied bytes are not interpreted.

- [base64.encode()](../functions_base64/base64.encode.md). All bytes of the binary input are used, as determined by the [byte capacity](data_types.md#byte capacity).

- [base64.decode()](../functions_base64/base64.decode.md). All bytes of the base64-encoded input are used, as determined by the [byte capacity](data_types.md#byte capacity).

## Record buffers as binary strings
A record buffer (rcd.<table name>) is a binary string. When data is copied to or from a record buffer, all bytes are copied without interpretation, which implies that 0-valued bytes are not interpreted as NULL-termination.
Such a copy action can result from a normal assignment, from passing a string as a call by value parameter to a function, or from the use of one of the functions [import()](../functions_variables_interprocess_transfer/import.md) or [export()](../functions_variables_interprocess_transfer/export.md). For example:
```

table  tttadv999

strbuf        = rcd.tttadv999   | all bytes are copied
rcd.tttadv999 = strbuf          | all bytes are copied
strbuf2       = strbuf          | NULL-terminated string from strbuf is copied (with zero-padding) to strbuf2
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Variables](variables.md)
