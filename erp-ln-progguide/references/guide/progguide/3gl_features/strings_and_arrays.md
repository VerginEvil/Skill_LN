# Strings and arrays
Strings and arrays are used to store multiple values of the same type within one named item. A string is a sequence of characters; subsequences of the string and individual characters can be accessed. Arrays are collections of equally typed elements; the elements can be accessed individually. When the individual elements of an array are of type string, the array is called a string array; its strings, subsequences of its strings and individual characters can be accessed.
An array can have up to four dimensions. For a string array, the length of the individual strings is considered as one of its maximally four dimensions. The dimensions of a string or array variable are specified between round brackets ( ) in a comma-separated list in the [declaration](declarations.md) of the variable.
There are three types of arrays: long, double, and string.

## Long arrays
The following example shows some declarations of long arrays.
```

LONG long_row(5)             | 1-dimensional array for 5 longs.

LONG long_matrix(4,5)        | 2-dimensional array for 4x5 longs:
                             | 4 rows of 5 longs.

LONG long_cube(3,4,5)        | 3-dimensional array for 3x4x5 longs:
                             | 3 matrices of 4 rows of 5 longs.

LONG long_hypercube(2,3,4,5) | 4-dimensional array for 2x3x4x5 longs:
                             | 2 cubes of 3 matrices of 4 rows of 5 longs.
```
The number of longs in the array is determined by the product of its dimensions.
Access to individual elements is specified by means of a bracketed and comma-separated list of indices after the name of the array.
Each index must be an expression of type long.
The number of indices must be equal to the number of dimensions of the array.
The indices are 1-based, i.e. each index must evaluate to at least the value 1 and to at most the value of the corresponding dimension.
As an example, consider the expression `long_cube( x, y, z )`, where `long_cube` is the array declared above as `LONG long_cube(3,4,5)`.
In the expression `long_cube( x, y, z )`, the index expressions x, y, and z must evaluate to long values obeying the following rules.
- x in the range [1 … 3]
- y in the range [1 … 4]
- z in the range [1 … 5]  A less relevant technical detail is that the dimensions are ordered from most significant to least significant. This means that the longs are stored in memory as indicated in the comments in the example above, e.g. `long_matrix` is stored in memory as 4 rows of 5 longs, not as 5 rows of 4 longs.
In other words: elements `long_matrix(1,1)` and `long_matrix(1,2)` are stored in neighboring memory positions, and also elements `long_matrix(1,5)` and `long_matrix(2,1)` are stored in neighboring memory positions.
As a further example, the following piece of code enumerates the elements of `long_cube` in the increasing order of their memory address and assigns increasing identification numbers to them. In the second part of the example the elements are enumerated in a different order.
```

LONG	long_cube( 3, 4, 5 )
LONG	x, y, z
LONG	identification

identification	= 0

FOR x = 1 TO 3	| outer for-loop: slowest changing index
	FOR y = 1 TO 4
		FOR z = 1 TO 5	| inner for-loop: fastest changing index
			| Use slowest changing index for most significant dimension.
			| Use fastest changing index for least significant dimension.
			| Notice that:
			|	identification = 20 * ( x - 1 ) + 5 * ( y - 1 ) + ( z - 1 ).

			long_cube( x, y, z )	= identification
			identification		= identification + 1
		ENDFOR
	ENDFOR
ENDFOR

FOR z = 1 TO 5	| outer for-loop: slowest changing index
	FOR y = 1 TO 4
		FOR x = 1 TO 3	| inner for-loop: fastest changing index
			identification	= long_cube( x, y, z )

			| Notice that, again:
			|	identification = 20 * ( x - 1 ) + 5 * ( y - 1 ) + ( z - 1 ),
			| so the elements are enumerated in the order:
			|	 0, 20, 40,
			|	 5, 25, 45,
			|	...,
			|	14, 34, 54,
			|	19, 39, 59.
		ENDFOR
	ENDFOR
ENDFOR
```

## Double arrays
A double array differs from a long array only in that its [declaration](declarations.md) uses the type DOUBLE instead of LONG and consequently the array elements are of type DOUBLE.

## Strings
A string is a (one-dimensional) sequence of characters. The length of the sequence is specified in the [declaration](declarations.md) of the string. In the following example, the variable `my_string` is declared as a string of length 10.
```

STRING my_string(10)
```
Substrings of a string variable can be accessed by specifying between round brackets the start position within the original string and optionally also the explicit substring length. By default (i.e. when no explicit length is specified) the substring extends to the end of the original string.
The start position and the explicit substring length must be expressions of type long.
The start position is 1-based, i.e. start position 1 specifies the begin of the underlying string.
When an explicit substring length is specified, it is separated from the preceding start position by a semicolon.
Individual characters of a string can be accessed by specifying them as a substring with explicit length 1.
The following code shows some examples of strings, substrings and individual characters.
```

STRING my_string(10)

my_string	= "abcdefghij"	| string variable my_string now contains string value "abcdefghij"

my_string(6)		| the substring starting at position 6 (and extending to the end of the string) contains string value "fghij"

my_string(6;2)		| the substring of length 2, starting at position 6, contains string value "fg"

my_string(6;1)		| the single character at position 6 is "f"

LONG	start
LONG	my_length

FOR start = 1 TO 10
	FOR my_length = 0 TO 10 - ( start - 1 )
		| arbitrary expressions of type long can be used to specify start point and substring length
		my_string( start ; my_length )	| the substring of length 'my_length', starting at position 'start'
	ENDFOR
ENDFOR
```
Use the [assignment operator](assignment_operator.md) to assign a string value to a string variable or to a substring of a string variable.

## String arrays
The following example shows some declarations of string arrays.
```

STRING string_matrix(5,4)       | 2-dimensional string array for 4x5 characters:
                                | 4 strings of 5 characters.

STRING string_cube(5,3,4)       | 3-dimensional string array for 3x4x5 characters:
                                | 3 matrices of 4 strings of 5 characters.

STRING string_hypercube(5,2,3,4)| 4-dimensional string array for 2x3x4x5 characters:
                                | 2 cubes of 3 matrices of 4 strings of 5 characters.
```
The number of characters in the string array is determined by the product of its dimensions.
The length of the individual strings in the string array is determined by its first dimension.
The number of strings in the string array is determined by the product of its second and further dimensions.
Access to an individual string or substring is specified by means of a bracketed and comma-separated list of indices after the name of the array, optionally followed (within the brackets) by a semicolon and an explicit substring length. By default (i.e. when no explicit length is specified) the substring extends to the end of the original string.
Each index and the explicit substring length must be an expression of type long.
The number of indices must be equal to the number of dimensions of the string array.
The indices are 1-based, i.e. each index must evaluate to at least the value 1 and to at most the value of the corresponding dimension.
The first index specifies the start position of the substring within the string specified by the other indices.
As an example, consider the expression `string_cube( s, x, y )`, where `string_cube` is the string array declared above as `STRING string_cube(5,3,4)`.
In the expression `string_cube( s, x, y )`, the index expressions s, x, and y must evaluate to long values obeying the following rules.
- s in the range [1 … 5]
- x in the range [1 … 3]
- y in the range [1 … 4]  The following code shows some examples of accessing a string, a substring and an individual character in a string array.
```

STRING string_array( 7, 8 )		| The array contains 8 strings of length 7

string_array( 1, 3 ) = "abcdefg"	| The third string now contains string value "abcdefg"

string_array( 4, 3 )		| the substring starting at position 4 (and extending to the end of the string) contains string value "defg"

string_array( 4, 3 ; 2 )		| the substring of length 2, starting at position 4, contains string value "de"

string_array( 4, 3 ; 1 )		| the single character at position 4 in the third string is "d"
```
A less relevant technical detail is that the dimensions (except the first one) are ordered from most significant to less significant. The first dimension is the least significant one. This means that the characters are stored in memory as indicated in the comments in the example above, e.g. `string_cube` is stored in memory as 3 matrices of 4 strings of 5 characters, not as 4 matrices of 3 strings of 5 characters.
In other words: characters `string_cube(1,1,1;1)` and `string_cube(2,1,1;1)` are stored in neighboring memory positions, strings `string_cube(1,1,1)` and `string_cube(1,1,2)` are stored as neighboring strings, and also characters `string_cube(5,1,4;1)` and `string_cube(1,2,1;1)` are stored in neighboring memory positions.
As a further example, the following piece of code enumerates the individual characters of `small_string_cube` in the increasing order of their memory address and assigns increasing alphabetic characters to them. In the second part of the example the characters are enumerated in a different order.
```

STRING	small_string_cube( 4, 2, 3 )	| 2 matrices of 3 strings of 4 characters
LONG	s, x, y

LONG	index
STRING	flat_string( 24 )

index		= 1
flat_string	= "abcdefghijklmnopqrstuvwx"

FOR x = 1 TO 2	| outer for-loop: slowest changing index
	FOR y = 1 TO 3
		FOR s = 1 TO 4	| inner for-loop: fastest changing index
			| Use slowest changing index for most significant dimension.
			| Use fastest changing index for least significant dimension.

			small_string_cube( s, x, y ; 1 )	= flat_string( index )
			index	= index + 1
		ENDFOR
	ENDFOR
ENDFOR

| The 2 matrices of 3 strings of length 4 in the string array were filled
| in increasing memory order and now they contain the following string values:
|
|	"abcd",
|	"efgh",
|	"ijkl",
|
|	"mnop",
|	"qrst",
|	"uvwx".

index		= 1
flat_string	= ""

FOR s = 1 TO 4	| outer for-loop: slowest changing index
	FOR y = 1 TO 3
		FOR x = 1 TO 2	| inner for-loop: fastest changing index
			flat_string( index ; 1 )	= small_string_cube( s, x, y ; 1 )
			index	= index + 1
		ENDFOR
	ENDFOR
ENDFOR

| The characters were enumerated in the following order,
| shown in 4 groups of 3 lines of 2 characters:
|
|	'a', 'm',
|	'e', 'q',
|	'i', 'u',
|
|	'b', 'n',
|	'f', 'r',
|	'j', 'v',
|
|	'c', 'o',
|	'g', 's',
|	'k', 'w',
|
|	'd', 'p',
|	'h', 't',
|	'l', 'x'.

| The variable flat_string now contains the value "ameqiubnfrjvcogskwdphtlx"
```
Use the [assignment operator](assignment_operator.md) to assign a string value to a string variable or to a substring of a string variable.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Variables](variables.md)
