# query.define.sort.order()

## Syntax:
`function long query.define.sort.order( long table.index, const string field.var, direction.var, [ const string...,... ] )`

## Description
With this function the direction of an index-field or the whole index of an table-index can be set.
The function overrides the direction of parts in the table-index only for the session.

## Use of direction index-part in session
| | |
|---|---|
| first | in the display and the process of the detail-lines (grid) |
| second | in the navigation through the groups of the header. The sql statement first, next, prev and last are changed. |
| third | in the session find. In the search instruction, the blank fields for a descending index are replaced at search time by high value. |
The function don't override the field sort order of an active filter.
You can use the function query.define.sort.order in the section before.program. In other sections it will activated with the function rebuild.query(). Per referenced key, one or more index fields with the direction can be set.

## Direction index-part in session
| | | | | |
|---|---|---|---|---|
| origin \ situation | A | B | C | D |
| asc/desc in filter | not present | not present | present | present |
| define sort order | not present | present | not present | present |
| result | from index | from define | from filter | from filter |
Note: With this function only the direction of a key field can be changed. With the field sort order in a filter the priority of a field can be changed. By example first ascending on field A, second descending on field B.
Note2: Do not use the function on big tables without using a limited view; as this could result in performance issues.

## Example 1: Change direction at startup
```

|****************************** program section ********************************
before.program:
	long ret

	| override on table index 1
	ret = query.define.sort.order(1,"aabbbbnnn.fld3", "desc", "aabbbbnnn.fld5", "desc" )
	if ( ret < 0 ) then
		message("An error occurred on query.define.sort.order index 1")
		...
	endif

	| override on table index 2
	ret = query.define.sort.order(2,"aabbbbnnn.fld5", "desc" )
	if ( ret < 0 ) then
		message("An error occurred on query.define.sort.order index 2")
		...
	endif

	| override whole index on table index 3
	ret = query.define.sort.order(3,"aabbbbnnn._index3", "desc" )
	if ( ret < 0 ) then
		message("An error occurred on query.define.sort.order index 3")
		...
	endif
```
NOTE: The combination of query.define.sort.order and use of combined field statement in the query.extend.where will give unpredictable results

## Arguments

## field order direction set
| | | |
|---|---|---|
| `long` | `table.index` |  Sequence number of the referenced table-index.  |
| `const string` | `field.var, direction.var` |  For each set, specify the order direction with the name of the relevant field and it's direction of sorting field.var: 1) Field must exist in the table index by parameter table.index or 2) the whole of the referenced table-index with name: *file*_index< *number* > field.var equals indexname cannot combined with another field.var. direction.var: Presentation direction, possible values direction "ASC" or "DESC".  |
| `[ const string` | `...,... ]` |  next pair of [field.var, direction.var]. Use these optional pair of arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -n | Negative value of the parameter with the wrong value. |
| -9999 | Too many parameters. The input exceeds the maximum number of index parts. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## TIV
This function is available from TIV level 1900.
field.var: is indexname is available from application TIV level 2020.

## Related topics
- [SQL query extensions synopsis](synopsis.md)
