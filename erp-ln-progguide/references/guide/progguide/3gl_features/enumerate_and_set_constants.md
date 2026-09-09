# Enumerate and set constants
In the data dictionary you can define database table fields and domains of type enumerate or set.
An enumerate or set domain consists of a number of constants. In the program script (and other places in the data dictionary), a symbolic name is used. The symbolic name is the domain name, followed by a period [.] followed by the name of the constant. Variables of type set can also consist of a combination of set values.

## Examples of enumerate constants
```

      DOMAIN color  box_color       | color is an enumerate domain
                                    | with two constants, green and red

      box_color = color.green
      box_color = color.red
```

## Examples of set constants
```

      DOMAIN feature cf                         | feature is a domain of type set with
                                                | the constants bold, reverse, underlined
      cf = feature.bold
      cf = cf + feature.reverse                 | add constant, cf contains
                                                | bold and reverse
      cf = cf - feature.bold                    | subtract constant
      etol( cf )                                | returns the combined number of the
                                                | current value, here reverse.
```
For working with sets, see also the [Bit operations: overview and synopsis](../functions_bit/bit_operations_overview_and_synopsis.md) functions.
A special constant of type enumerate or set is EMPTY. This indicates an empty set or an enumerate that is not defined. Internally, it has the value 0.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Constants](constants.md)
