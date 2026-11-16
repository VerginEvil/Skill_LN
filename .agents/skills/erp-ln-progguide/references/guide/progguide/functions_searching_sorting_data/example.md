# Table searching and sorting sample programs

## Example 1
You want to sort the following (string) array. The number is stored as a long on positions 8 to 11 by means of the function store.long(number, string_array(8,n))
```

    string    string_array(11,5)
    long      sort_def(2,4), search_def(1,4), ret

    string_array(1,1) = "hhhh"    store.long(3,string_array(8,1))
    string_array(1,2) = "dddd"    store.long(2,string_array(8,2))
    string_array(1,3) = "zzzz"    store.long(1,string_array(8,3))
    string_array(1,4) = "pppp"    store.long(3,string_array(8,4))
    string_array(1,5) = "iiii"    store.long(1,string_array(8,5))

    qss.start(sort_def, 1, 8)
    qss.way(sort_def, 1, QSS.UP)
    qss.type(sort_def, 1, DB.LONG)

    qss.start(sort_def, 2, 1)
    qss.way(sort_def, 2, QSS.DOWN)
    qss.type(sort_def, 2, DB.STRING)
    qss.length(sort_def, 2, 5)
    | The function executes an ascending sort on position 8 of the
    | string. The sort must be carried out as if this is a long value.
    | In case of equal values, a descending sort is performed on the
    | first five characters of the string.

    ret = qss.sort(string_array, sort_def)

    | After sorting the array will look as follows:
```
```

    | If you want to know in which element the character combination
    | 'iii' occurs as the 2nd, 3rd and 4th character, and are sure that
    | the argument to be searched is unique and cannot occur in the last
    | two elements, the following search action can be started.
    | It is assumed that the array is sorted.

    qss.start(search_def, 1, 2)          | search from position 2
    qss.length(search_def, 1, 3)         | search key is 3 characters long
    qss.type(search_def, 1, DB.STRING)
	qss.way(search_def, 1, QSS.DOWN)

    ret = qss.search(QSS.SRC.IS.SORTED + QSS.EQUAL, "iii",
                    string_array, search_def, 3)
    | ret will now contain the value 2
    | if the search argument is not unique, the following search
    | action may be started:
    ret = qss.search(QSS.SRC.IS.SORTED + QSS.EQUAL +
             QSS.SRC.DUPL.ALLOWED, "iii",
             string_array, search_def, 3)
```

## Example 2
```

    string  key(50)
    string  bank(50,10)
    long    country(2,4)        | Key on country code and bank number
    long    sort_def(1,4)
    long    index

    |                     1         2         3         4         5
    |            12345678901234567890123456789012345678901234567890
    bank(1,1) = "10010ING                           Utrecht     NL "
    bank(1,2) = "10020ABN / AMRO                    Amsterdam   NL "
    bank(1,3) = "10030Rabobank                      Ede         NL "
    bank(1,4) = "20020National Westminster Bank     London      GB "
    bank(1,5) = "30010Sparkasse                     Munchen     D  "
    bank(1,6) = "40010Credit Lyonnais               Paris       F  "
    bank(1,7) = "90010Citi Bank                     New York    USA"
    bank(1,8) = "90020NBD Bank                      Grand RapidsUSA"

    qss.start (country, 1, 48)
    qss.type  (country, 1, DB.STRING)
    qss.length(country, 1, 3)
    qss.start (country, 2, 1)
    qss.type  (country, 2, DB.STRING)
    qss.length(country, 2, 5)

    | WITHOUT LOOKUP.FOR.STRUCT
    key = "NL"
    index = qss.search(QSS.GTEQ, key, bank, country)
    while index > 0 and bank(48,index;3) = "NL "
            | process struct
            key = bank(48,index;3) & bank(1,index;5)
            index = qss.search(QSS.GT, key, bank, country )
    endwhile

    | WITH LOOKUP.FOR.STRUCT
    key = "                                               NL "
    index = qss.search(QSS.LOOKUP.FOR.STRUCT+QSS.GTEQ,
                key, bank, country)
    while index > 0 and bank(48,index;3) = "NL "
                    | process struct
            index = qss.search(QSS.LOOKUP.FOR.STRUCT+QSS.GT,
                    bank(1,index), bank, country)
    endwhile

    | Sorting bank table on bank description

    qss.start (sort_def, 1, 6)
    qss.type  (sort_def, 1, DB.STRING)
    qss.length(sort_def, 1, 2)

    index = qss.sort( bank, sort_def)
```

## Related topics
- [Searching and sorting data overview and synopsis](overview_and_synopsis.md)
