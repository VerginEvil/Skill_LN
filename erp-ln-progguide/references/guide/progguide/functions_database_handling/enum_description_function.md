# ENUM_DESCRIPTION function
With the ENUM_DESCRIPTION function you can retrieve the description for the enumeration value of a column.

## Syntax
```

<enum description function>
    ::= ENUM_DESCRIPTION ( Column reference [ , String constant ] )
```

## Syntactical restrictions
The *<column reference>* shall identify a column that is an enumeration.
The length of the optional *<string constant>* argument shall be 1.

## Semantics
The data type of the result of the ENUM_DESCRIPTION function is *string*.
The optional *<string constant>* argument identifies the language for the description. If *<string constant>* is omitted then the current language of the user will be used. If the description is not available in the specified language then language code '2' (that is: English) is used.

## Examples
The following ENUM_DESCRIPTION function returns the description for the value of the column *dbtst120.sex*, which is either 'Male' or 'Female'.
```

ENUM_DESCRIPTION( dbtst120.sex, '2' )
```

## Related topics
- [Column reference](column_reference.md)
- [Infor Enterprise Server SQL](baan_sql.md)
