# make.path.absolute()

## Syntax:
`function long make.path.absolute( ref string path_name )`

## Description
Makes path absolute given in *path_name*. It gives the full path back also in *path_name*.

## Arguments
| | | |
|---|---|---|
| `ref string` | `path_name` |  path  |

## Return values
| | |
|---|---|
| 0 | Success. |
| other value | Errror. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
