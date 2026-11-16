# Variables (checking changes): sample program
```

string   city(10)

city = "Paris"
on.change.check( city )   | checkpoint value set to Paris
city = "Rotterdam"
on.change.check( city )   | checkpoint value now set to Rotterdam
city = "Amsterdam"
if ( changed(city) ) then | changed() returns TRUE here, but also sets
              |    the new checkpoint value to "Amsterdam"
        not.curr( city )
        message( "City is changed, old city is: %s",city )  | city is Rotterdam
        not.curr( city )
        message( "New city is: %s",city )   | city is Amsterdam
endif
off.change.check(city)
```

## Related topics
- [Variables (checking changes) overview](overview.md)

- [Variables (checking changes) synopsis](synopsis.md)
