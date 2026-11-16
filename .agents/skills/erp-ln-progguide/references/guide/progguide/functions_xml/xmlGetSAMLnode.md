# Get SAML (security data) node

## Syntax:
`function long xmlGetSAMLnode( )`

## Description
Get the root-node of the XML document that contains the SAML (Security Assertion Markup Language) data that has been passed by the security and authentication system. This will contain details about the user, authentication and authorisation data.
This data is provided by the bshell as a read-only XML-tree: it must not be altered in any way.

## Return values
| | |
|---|---|
| 0 | Failure. There is no SAML data avaliable. |
| <> 0 | The root-node of the XML document that contains the SAML data. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
