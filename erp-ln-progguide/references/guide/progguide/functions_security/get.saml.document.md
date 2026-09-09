# get.saml.document

## Syntax:
`function string get.saml.document( )`

## Description
Returns the document that contains the SAML (Security Assertion Markup Language) data that has been passed by the security and authentication system. This will contain details about the user, authentication and authorisation data. This data is provided by the bshell. It cannot be modified.

## Return values
The return value is an empty string when no SAML document was provided

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

function void main()
{
	string saml.doc(64*1024) | note: SAML documents can be quite large. Use str.assign()

	saml.doc = get.saml.document()
}
```

- SAML documents can be quite large. Ensure enough memory for the return string.
