# Function type and return value
The type declaration in a function declaration indicates the type of the function. Functions can be of the following types:
- long
- double
- string
- domain
- void (this means that no value is returned)  If you do not specify a type, the function is of type void by default.
The type of a function indicates the (compile time) type of its return value.
A function of type void does not have a return value. Any return statement in such a function must not have any argument.
For a non-void function, the type of the return value must be equal to the type of the function.
Apart from the general rule above, it is allowed to return a value of type long from a function of type double. No conversion is done, so the run time type of the return value is long, which differs from the double compile time type.
Apart from the general rule above, it is allowed to return a value of type double from a function of type long. No conversion is done, so the run time type of the return value is double, which differs from the long compile time type.
Some examples:
```

function f()   | function without return type is of type void
{
        return | no value is returned
}

function long  return.as.long(   | function of type long
   boolean  aConvert,
   double   aDouble
)
{
   if aConvert then
      long  lLong

      lLong = aDouble   | assignment of double value to long variable.
                        | implicit double to long type conversion is done.

      return(lLong)     | long value returned from long function
   else
      return(aDouble)   | double value returned from long function
   endif
}

function double  return.as.double(   | function of type double
   boolean  aConvert,
   long     aLong
)
{
   if aConvert then
      double   lDouble

      lDouble  = aLong  | assignment of long value to double variable.
                        | implicit long to double type conversion is done.

      return(lDouble)   | double value returned from double function
   else
      return(aLong)     | long value returned from double function
   endif
}
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Functions](functions.md)
