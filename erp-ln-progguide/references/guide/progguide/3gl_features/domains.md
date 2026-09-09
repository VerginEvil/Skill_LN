# Domains
When declaring temporary variables for storing values of database fields, you can use normal variables of type long, double, or string. But this can cause problems if the length or type of the table field has been changed in the data dictionary. It is preferable to use domain declarations for storing the value of a database table field. When you use a domain declaration, the type and length for the declared variable are read from the data dictionary.
Variables of type enumerate or set must always be declared with a domain declaration.
It is also possible to declare an array by using a domain. In that case the number of elements must be set between the brackets, the length of the elements is embedded in the data dictionary.

## Examples
The following examples illustrate various domain declarations, and the declaration of the same variables without domains.
DOMAIN declarations
```

DOMAIN  tst_str10   tmp_str,          | String of length 10
                    tmp_str_arr(100)  | 100 strings of length 10
DOMAIN  tst_long    tmp_lng1,         | A long number
                    tmp_lng2,         | Another long number
                    tmp_lng_matr(5,2) | A matrix 5 x 2
DOMAIN  tst_double  tmp_dbl,          | A floating point
                    tmp_dbl_arr(100)  | 100 floating points
```
STRING declarations
```

#define LENG 10
STRING  tmp_str(LENG),                | String of length 10
        tmp_str_arr(LENG*10,10)       | 10 strings of length 100
```
LONG declarations
```

LONG    tmp_lng1,                     | A long number
        tmp_lng2,                     | Another long number
        tmp_lng_matr(5,2)             | A matrix 5 x 2
```
DOUBLE declarations
```

#define MAXLEN 1000
DOUBLE  tmp_dbl,                      | A floating point
        tmp_dbl_array(MAXLEN/10)      | MAXLEN/10 floating points
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Variables](variables.md)
