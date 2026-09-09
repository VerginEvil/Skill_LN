# References

## Retrieving references to a record
In the standard SQL interface, you can retrieve references to a record as follows:
```

| Suppose that tiitm001 has a reference to tccom010 (field 'cuno'),
| and to tccom011 (field 'suno')
table  ttiitm001
table  ttccom010
table  ttccom011

SELECT tiitm001.*, tccom010.*, tccom011.*
FROM   tiitm001, tccom010, tccom011
WHERE  tiitm001.cuno = tccom010.cuno
AND    tiitm001.suno = tccom011.suno
```

## Retrieving references using REFERS TO
To simplify the retrieval of references, you can specify references (using the keyword REFERS TO) in the WHERE clause. Apart from simplifying the query, this also optimizes query handling. As references always refer to a primary key, they can be found immediately. Moreover, the program fills a field with reference characters if it does not find a reference. The following implements the previous example by using REFERS TO:
```

table  ttiitm001
table  ttccom010
table  ttccom011

SELECT tiitm001.*, tccom010.*, tccom011.*
WHERE  tiitm001.cuno REFERS TO tccom010
AND    tiitm001.suno REFERS TO tccom011
```

## REFERS TO syntax
A REFERS TO predicate has the following form:
```

<from> REFERS TO <to> [ PATH <path> [ { , <path> }... ] ] [ UNREF <mode> ]
```
The following table explains the various parts of the predicate:
```
<from>
```
```
<to>
```
```
<path>
```
```

WHERE table1.field REFERS TO table4.field PATH table2.field, table3.field
```
```
<mode>
```
| | |
|---|---|
| SKIP | If a reference cannot be found, the record is skipped. |
| CLEAR | If a reference is empty or absent, the referring record is filled with spaces or 0 (numeric). |
| SETUNREF | The value of an undefined reference is filled with an 'undefined reference' sign, defined in the data dictionary, or with 0 (numeric). |
| CLEARUNREF | The referred record is filled with spaces or 0 (zero) when reference fields are empty. When the reference is undefined the referred record is filled with an 'undefined reference' sign. |
Depending on the reference definition in the data dictionary, the default reference mode is:
| | |
|---|---|
| reference mode in DD | UNREF mode |
| mandatory | SETUNREF |
| mandatory unless empty | CLEARUNREF |
| not mandatory | CLEAR |

## Example
```

SELECT ttadv100.*
FROM   ttadv100, ttadv101
WHERE  ttadv101.cmod BETWEEN "aaa" AND "azz"
AND    ttadv101 REFERS TO ttadv100 UNREF <UNREF_mode>
AND    ttadv100.cpac BETWEEN "  " AND "zz"
```
The evaluation order of this query may be as follows:

- Find all rows / records in ttadv101 that match the BETWEEN "aaa" AND "azz" condition.

- Find all references from each row from step 1 in table ttadv100.

- Find all rows selected in step 2 which match the BETWEEN " " AND "zz" condition

When some reference does not exist in ttadv100 (step 2 fails), because of the condition on the referenced table, the whole row is rejected.

## Using aliases with REFERS TO
You can use aliases to refer from one table to another with two references. In the following example, there are two references from ttadv300 to ttaad110, via ttadv300.lanl and via ttadv300.clan. Both are searched for in the following construction:
```

string desc.clan(20), desc.lanl(20)
table  tttadv300

SELECT ttadv300.desi, ttadv300.cfrm, ttadv300.clan,
       tclan.dsca:desc.clan, ttadv300.lanl, tlanl.dsca:desc.lanl
FROM   ttadv300, ttaad110 tlanl, ttaad110 tclan
WHERE  ttadv300.desi = :designer
AND    ttadv300.clan REFERS TO tclan UNREF SETUNREF
AND    ttadv300.lanl REFERS TO tlanl UNREF SETUNREF
```

## Using program variables or constants with REFERS TO
You can also retrieve references by using a program variable or a constant. This avoids the program first reading the <from> table. In the following example tiitm001 has a reference to tccom010 (field 'cuno'), and a reference to tccom011 (field 'suno') and the value of tiitm001 is known:
```

table  ttccom010
table  ttccom011

SELECT tccom010.*, tccom011.*
FROM   tccom010, tccom011
WHERE  :tiitm001.cuno = tccom010.cuno
AND    :tiitm001.suno = tccom011.suno
```
In the following example, the REFERS TO predicate is used to achieve the same result. If the program does not find the reference, it fills the field with reference characters.
```

table  ttccom010
table  ttccom011

SELECT tccom010.*, tccom011.*
WHERE  :tiitm001.cuno REFERS TO tccom010
AND    :tiitm001.suno REFERS TO tccom011
```
In this case the REFERS TO predicate has the following form:
```

<from> REFERS TO <to> [ UNREF <mode> ]
```
The following table explains the various parts of the predicate:
```
<from>
```
```
<to>
```
```
<mode>
```
| | |
|---|---|
| SKIP | If a reference cannot be found, the record is skipped. |
| CLEAR | If a reference is empty or absent, the referring record is filled with spaces or 0 (numeric). |
| SETUNREF | The value of an undefined reference is filled with an 'undefined reference' sign, defined in the data dictionary, or with 0 (numeric). |
| CLEARUNREF | The referred record is filled with spaces or 0 (zero) when reference fields are empty. When the reference is undefined the referred record is filled with an 'undefined reference' sign. |
As no dictionary default is available, SETUNREF has been defined as the default action.

## Example
```

SELECT tccom010.*
FROM   tccom010, tiitm001
WHERE  tiitm001.cuno = :tiitm001.cuno
AND    tiitm001.cuno REFERS TO tccom010
```
This is equal to the following:
```

SELECT tccom010.*
WHERE  :tiitm001.cuno REFERS TO tccom010
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
