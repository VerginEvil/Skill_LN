# SQL and combined fields
Defining a query that can be handled efficiently by the query handler is a complex task. This is especially true if there are combined fields (which consist of a number of child fields), as each field must be specified separately.

## Specifying a combined field
As the designer can usually judge best which index should be used for an optimum result, the following construction enables the designer to specify a combined field:
```

WHERE ppmod001.comb1 = {"adv", "099", "123"}
```
A child field can be an expression, a BAAN 4GL variable, or a pseudo variable. A comparison operator (=, >, >=, etc.) for a combined field applies to the combination of all child fields. For example:
```

| suppose the combined field ppmod001.comb1 consists of the
| fields ppmod001.modu, ppmod001.tblno and ppmod001.compno:
WHERE ppmod001.comb1 >= {"adv", "000", "100"}
| The above statement is equal to the following statement
WHERE ( ppmod001.modu > "adv" ) OR
      ( ppmod001.modu = "adv" AND ppmod001.tblno > "000" ) OR
      ( ppmod001.modu = "adv" AND ppmod001.tblno = "000" AND
        ppmod001.compno >= "100" )
```

## Comparison operators for combined fields
The comparison operators #>, #>=, #<, #<= for a combined field apply to each child field separately. For example:
```

WHERE       ( ppmod001.comb1 #>= {"adv", "000", "100"} AND
         ppmod001.comb1 #<= {"zzz", "999", "200"} )
```
This represents the following:
```

WHERE       ppmod001.modu >= "adv" AND ppmod001.modu <= "zzz" AND
       ppmod001.tblno >= "000" AND ppmod001.tblno <= "999" AND
       ppmod001.compno >= "100" AND ppmod001.compno <= "200"
```
If a child field of a combined field is not specified, the value of this field is free and is not included in the condition. For example:
```

WHERE       ppmod001.comb1 #>= {"adv", "000", "100"} AND
       ppmod001.comb1 #<= {"zzz", "999"}
```
This represents the following:
```

WHERE       ppmod001.modu >= "adv" AND ppmod001.modu <= "zzz" AND
       ppmod001.tblno >= "000" AND ppmod001.tblno <= "999" AND
       ppmod001.compno >= "100"
```
As the field ppmod001.compno has no upper limit, all values greater than or equal to 100 are fetched.

## Indexes as combined fields
You can specify an index as a combined field even if a combined field is not present in the data dictionary. The index name is table._indexY where:
| | |
|---|---|
| table | is the name of the table or alias of a table |
| _index | is a prefix to indicate that an index field is involved (a condition for this syntax is that there are no field names having this format) |
| Y | is the sequence number of the index defined in the data dictionary |
As a combined field is being used, the value must always be enclosed by '{' and '}'. For example:
```

WHERE tiitm001._index1 = {:item }
```
As with other combined fields, children of index fields for which no value is specified are not included in the condition. However, you can leave fields unspecified only at the end of the index, not in the middle.
An index's pseudo field cannot be used in the query preceded by ':'.

## Meanings of upper and lower limits
In connection with combined fields, the combination of upper/lower limit can have two meanings (compare '>' and '#>').

- Firstly, it can mean that each field of a record that meets the conditions lies between the boundaries specified. For example: `WHERE ( ppmod001.comb1 #>= {"adv", "000", "100"} AND ppmod001.comb1 #<={"zzz", "999", "200"} )` Here, {"adv", "050" "123"} meet the conditions, but the combination {"uvw", "123", "300"} does not, because of the last child field.For this construction we define the INRANGE statement. With INRANGE, the preceding example becomes: `WHERE ppmod001.comb1 INRANGE {"adv", "000","100"} AND {"zzz", "999", "200"}` With INRANGE, the boundaries indicated apply to each separate field (usual in print sessions).

- Secondly, it can mean that all records are selected for which the combined field (regarded as one single field) lies between the boundaries indicated. For example: `WHERE ( ppmod001.comb1 >= {"adv", "000", "100"} AND ppmod001.comb1 <= {"zzz", "999", "200"} )` Here, {"uvw", "123", "300"} meets the condition as "uvw"&"123"&"300" lies between "adv"&"000"&"100" and "zzz"&"999"&"200" ('&' means concatenation).For this purpose we use a BETWEEN statement. With BETWEEN, the preceding example becomes: `WHERE ppmod001.comb1 BETWEEN {"adv", "000","100"} AND {"zzz", "999", "200"}` With BETWEEN, the fields in the combined are regarded as one field; the boundaries apply to the combined field as a whole.

If the field consists of one single element, INRANGE and BETWEEN are equivalent.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
