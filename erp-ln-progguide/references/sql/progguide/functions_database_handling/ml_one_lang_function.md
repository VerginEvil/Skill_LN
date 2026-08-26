# ml_one_lang function
With the ml_one_lang function you can select a single data language from a Multi Language Field (MLF). An MLF is a column which is configured to have multiple data languages.
When it is not necessary to retrieve all languages and a statement is very critical for performance it is possible to use this function, to avoid selecting the translations from the database. Do not do this in cases where the selected data is later inserted into the database, because this will lead to loss of the other translations of the value.

## Syntax
```

<ml_one_lang function>
    ::= ml_one_lang ( <column> [, <data language> | <parameter>] )

<column>
    ::= Column reference

<data language>
    ::= String constant

<parameter>
    ::= Parameter
```

## Syntactical restrictions
The *<data language>* (either as a constant or as a parameter) shall be a Data Language code in ISO 639-2 format, like "en_GB" for English, or "nl_NL" for Dutch.

## Semantics
If the column reference is not a Multi Language Field (MLF) then the function ml_one_lang returns the column value.
If *<string constant>* is omitted then the implicit string constant is the current data language of the user.

## Examples
The following ml_one_lang function returns the current language value of the column `dscr`.
```

select ml_one_lang(a.dscr) from dbtst100 a where a.id = 10
```
The following ml_one_lang function returns the french language value of the column `dscr`.
```

select ml_one_lang(a.dscr, 'fre') from dbtst100 a where a.id = 10
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
- [Multi Language Data](multi_language_data.md)
