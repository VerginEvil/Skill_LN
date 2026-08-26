# rsa.verify.signature

## Syntax:
`function boolean rsa.verify.signature( const string pub_key_file, long digest_type, string digest, const string signature )`

## Description
It verifies the digital signature signed with private key against the digest of the document calculated with the algorithm used for signing the document using the public key of the private-public key pair.

## Arguments
| | | |
|---|---|---|
| `const string` | `pub_key_file` |  The public key of the private-public key pair.  |
| `long` | `digest_type` |  The digest used for signing the document  |
| `string` | `digest` |  The digest calculated against the original document to be verified. This is the hex encoded as given by digest function in 3GL.  |
| `const string` | `signature` |  The signature is the base64 encoded string of the signature created when signing the document.  |

## Return values
true Success. false Error.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

function void main()
{
	string public_key_file(512)
	string digest(128)
	string signature(1024)
	boolean ret
	public_key_file="/tmp/publickey.pem"
	| Digest against the original document/string
	digest="87A727A9E3399D421D77C8F8D18EED0E241A570BAA0CE032F7175D41D16E77EA"
	| base64 encoded signature string
	signature="YaftNegpBn2mox5Z3IGzG1TBkMyjGBaL3y6z0eFmarUie/0BauJPwCMJmkga2se0gU/rqTIeHZc8 idwGdZaN6w+TQMMhmE9TOx+FgzkGZKEPLbNT1FWws8E8h3ysJSECdsC/Y6oRt6EpRu9s2n2hOMQx IdMS9xuyeqm4317Y1kI="
	| Verify the signature, return true on success
	ret=rsa.verify.signature(public_key_file,DIGEST_SHA256,digest,signature);
}
```
Notes
- This function is available in all TIV conditionally with the USE_RSA_ENCRYPT_FUNCTION compiler flag. The compiler flag can be defined as -D USE_RSA_ENCRYPT_FUNCTION.
