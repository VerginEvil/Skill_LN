# JSON synopsis

## General JSON value functions
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
boolean
```
```
double
```
```
boolean
```
```
long
```
```
double
```
```
string
```
```
long
```
```
long
```
```
void
```
```
[long]
```
```
long
```
```
boolean
```
```
long
```
| | | |
|---|---|---|
|  | [Json.newObject](Json_newObject.md) | `()` |
|  | [Json.newArray](Json_newArray.md) | `()` |
|  | [Json.newBoolean](Json_newBoolean.md) | `( boolean value )` |
|  | [Json.newDouble](Json_newDouble.md) | `( double value )` |
|  | [Json.newLong](Json_newLong.md) | `( long value )` |
|  | [Json.newNull](Json_newNull.md) | `()` |
|  | [Json.newNumber](Json_newNumber.md) | `( long|double value )` |
|  | [Json.newString](Json_newString.md) | `( const string value )` |
|  | [Json.boolean](Json_boolean.md) | `( long json_value )` |
|  | [Json.double](Json_double.md) | `( long json_value )` |
|  | [Json.isNull](Json_isNull.md) | `( long json_value )` |
|  | [Json.long](Json_long.md) | `( long json_value )` |
|  | [Json.number](Json_number.md) | `( long json_value )` |
|  | [Json.string](Json_string.md) | `( long json_value )` |
|  | [Json.copy](Json_copy.md) | `( long json_value )` |
|  | [Json.copyToProcess](Json_copyToProcess.md) | `( long json_value, long process_id )` |
|  | [Json.delete](Json_delete.md) | `( long json_value )` |
|  | [Json.detach](Json_detach.md) | `( long json_value )` |
|  | [Json.type](Json_type.md) | `( long json_value )` |
|  | [Json.isJson](Json_isJson.md) | `( long json_value )` |
|  | [Json.path](Json_path.md) | `( long json_value,... )` |

## JSON object functions
```
[long]
```
```
boolean
```
```
long
```
```
void
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
boolean
```
```
double
```
```
long
```
```
double
```
```
string
```
| | | |
|---|---|---|
|  | [Json.set](Json_set.md) | `( long json_object, const string key, long json_value )` |
|  | [Json.has](Json_has.md) | `( long json_object, const string key )` |
|  | [Json.get](Json_get.md) | `( long json_object, const string key )` |
|  | [Json.del](Json_del.md) | `( long json_object, const string key )` |
|  | [Json.setBoolean](Json_setBoolean.md) | `( long json_object, const string key, boolean value )` |
|  | [Json.setDouble](Json_setDouble.md) | `( long json_object, const string key, double value )` |
|  | [Json.setLong](Json_setLong.md) | `( long json_object, const string key, long value )` |
|  | [Json.setNull](Json_setNull.md) | `( long json_object, const string key )` |
|  | [Json.setNumber](Json_setNumber.md) | `( long json_object, const string key, long|double value )` |
|  | [Json.setString](Json_setString.md) | `( long json_object, const string key, const string value )` |
|  | [Json.getBoolean](Json_getBoolean.md) | `( long json_object, const string key )` |
|  | [Json.getDouble](Json_getDouble.md) | `( long json_object, const string key )` |
|  | [Json.getLong](Json_getLong.md) | `( long json_object, const string key )` |
|  | [Json.getNumber](Json_getNumber.md) | `( long json_object, const string key )` |
|  | [Json.getString](Json_getString.md) | `( long json_object, const string key )` |

## JSON array functions
```
[long]
```
```
[long]
```
```
[long]
```
```
long
```
```
void
```
```
long
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
[long]
```
```
boolean
```
```
double
```
```
long
```
```
double
```
```
string
```
| | | |
|---|---|---|
|  | [Json.add](Json_add.md) | `( long json_array, long json_value )` |
|  | [Json.insert](Json_insert.md) | `( long json_array, long idx, long json_value )` |
|  | [Json.put](Json_put.md) | `( long json_array, long idx, long json_value )` |
|  | [Json.at](Json_at.md) | `( long json_array, long idx )` |
|  | [Json.remove](Json_remove.md) | `( long json_array, long idx )` |
|  | [Json.count](Json_count.md) | `( long json_array )` |
|  | [Json.addBoolean](Json_addBoolean.md) | `( long json_array, boolean value )` |
|  | [Json.addDouble](Json_addDouble.md) | `( long json_array, double value )` |
|  | [Json.addLong](Json_addLong.md) | `( long json_array, long value )` |
|  | [Json.addNull](Json_addNull.md) | `( long json_array )` |
|  | [Json.addNumber](Json_addNumber.md) | `( long json_array, long|double value )` |
|  | [Json.addString](Json_addString.md) | `( long json_array, const string value )` |
|  | [Json.insertBoolean](Json_insertBoolean.md) | `( long json_array, long idx, boolean value )` |
|  | [Json.insertDouble](Json_insertDouble.md) | `( long json_array, long idx, double value )` |
|  | [Json.insertLong](Json_insertLong.md) | `( long json_array, long idx, long value )` |
|  | [Json.insertNull](Json_insertNull.md) | `( long json_array, long idx )` |
|  | [Json.insertNumber](Json_insertNumber.md) | `( long json_array, long idx, long|double value )` |
|  | [Json.insertString](Json_insertString.md) | `( long json_array, long idx, const string value )` |
|  | [Json.putBoolean](Json_putBoolean.md) | `( long json_array, long idx, boolean value )` |
|  | [Json.putDouble](Json_putDouble.md) | `( long json_array, long idx, double value )` |
|  | [Json.putLong](Json_putLong.md) | `( long json_array, long idx, long value )` |
|  | [Json.putNull](Json_putNull.md) | `( long json_array, long idx )` |
|  | [Json.putNumber](Json_putNumber.md) | `( long json_array, long idx, long|double value )` |
|  | [Json.putString](Json_putString.md) | `( long json_array, long idx, const string value )` |
|  | [Json.booleanAt](Json_booleanAt.md) | `( long json_array, long idx )` |
|  | [Json.doubleAt](Json_doubleAt.md) | `( long json_array, long idx )` |
|  | [Json.longAt](Json_longAt.md) | `( long json_array, long idx )` |
|  | [Json.numberAt](Json_numberAt.md) | `( long json_array, long idx )` |
|  | [Json.stringAt](Json_stringAt.md) | `( long json_array, long idx )` |

## JSON iterator functions
```
long
```
```
string
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [Json.iter](Json_iter.md) | `( long json_array|json_object )` |
|  | [Json.iterKey](Json_iterKey.md) | `( long json_object, long iter )` |
|  | [Json.iterNext](Json_iterNext.md) | `( long json_array|json_object, long iter )` |
|  | [Json.iterValue](Json_iterValue.md) | `( long json_array|json_object, long iter )` |

## JSON read/write functions
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [Json.read](Json_read.md) | `( long stream, ref string error_str, [long options] )` |
|  | [Json.readFile](Json_readFile.md) | `( const string path, ref string error_str, [long options] )` |
|  | [Json.readString](Json_readString.md) | `( const string json_str, ref string error_str, [long options] )` |
|  | [Json.write](Json_write.md) | `( long json_value, long stream, [long options] )` |
|  | [Json.writeFile](Json_writeFile.md) | `( long json_value, const string path, [long options] )` |
|  | [Json.writeString](Json_writeString.md) | `( long json_value, ref string str, [long options] )` |

## Related topics
- [JSON overview](JSon_object_overview.md)
