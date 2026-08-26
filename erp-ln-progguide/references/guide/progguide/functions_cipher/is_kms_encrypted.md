# is_kms_encrypted()

## Syntax:
`function boolean is_kms_encrypted( string encrypted_password )`

## Description
Determines if an encrypted password is encrypted with the KMS encryption function.

## Arguments
| | | |
|---|---|---|
| `string` | `encrypted_password` |  An encrypted string.  |

## Return values
| | |
|---|---|
| 0 | False. The string is not KMS encrypted. |
| 1 | The string looks like it is encrypted with KMS. The function only looks at the lead-in of the string, if that is "$1AWSKMS$" it will return TRUE, else FALSE.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Related topics
- [Cipher Functions overview](cipher_overview.md)
- [Cipher Function synopsis](cipher_synopsis.md)
