# rsa.create.signature$()

## Syntax:
`function string rsa.create.signature$()( const string message, const string scrambled.private.key, [ ref long signlen, ref string errormsg ] )`

## Description
Creates a base-64 encoded signature with a RSA private key

## Arguments
| | | |
|---|---|---|
| `const string` | `message` |  The input string  |
| `const string` | `scrambled.private.key` |  A private key in PEM format and scrambled  |
| `[ ref long` | `signlen ]` |  The length of the returned string. The return value of this function need to be assigned to a string variable with at least the length of *signlen*.  |
| `[ ref string` | `errormsg ]` |  An error message is returned, in case of something went wrong in bshell or underlying OpenSSL libraries. The error message may be cut off if the receiving variable has insufficient space to hold the whole error message. A string buffer of 512 bytes should be sufficient in most cases.  |

## Return values
The return value is an empty string in case of error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

#define PRIV_KEY
^ "$1R$xxxxyyyyzzz111222D74D3C32853B81545BD17F3FA8396C8E0DA024FCA38" &
...
^ "ABCDEF1234567890ABCDEF1234567890ABCD"

function void main()
{
	string errmsg(512)
	string msg(512)
	string sign(512)
	long signlen

	msg = "A user provided message"
	sign = rsa.create.signature$(msg, PRIV_KEY, signlen, errmsg)
}
```

- The shown private key in this example is not a valid key.

- The length of the output signature is fixed for any *msg* and a given private key. The length of the signature may change if a different (type of) private key is used.
