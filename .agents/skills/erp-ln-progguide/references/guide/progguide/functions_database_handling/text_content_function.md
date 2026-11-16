# TEXT_CONTENT function
With the TEXT_CONTENT function you can retrieve the text content for a column that is a text reference.

## Syntax
```

<text content function>
    ::= TEXT_CONTENT ( <column reference> [ , <string constant> ] )
```

## Syntactical restrictions
The *<**column reference**>* shall identify a column that is a text reference.
The length of the optional *<**string constant**>* argument shall be 1.

## Semantics
The data type of the result of the TEXT_CONTENT function is *string*.
The optional *<**string const**>* argument identifies the language for the text content. If *<**string const**>* is omitted then the current language of the user will be used.
If a text description does not exist (so the text number is for the specified language not available in the text table) then the result is a NULL value.

## Examples
The following TEXT_CONTENT function returns the text content for the text reference column *dbtst107.text*.
```

TEXT_CONTENT( dbtst107.text )
```

## Related topics
- [Column reference](column_reference.md)

- [Infor Enterprise Server SQL](baan_sql.md)
