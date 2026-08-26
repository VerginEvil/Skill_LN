# rsa.encrypt

## Syntax:
`function long rsa.encrypt( const string pub_key_file, const string data_in, long data_in_len, long padding_scheme, ref string output )`

## Description
The function encrypts the input string ( data_in) using the padding specified with padding_scheme parameter with the public_key_file and rsa algorithm . It returns the encrypted output as a (base64)Encoded string.

## Arguments
| | | |
|---|---|---|
| `const string` | `pub_key_file` |  The public key file to be used for encoding.  |
| `const string` | `data_in` |  The data to be encrypted  |
| `long` | `data_in_len` |  Length of input string ( if -1 is given, then the length of the input string is calculated by function).  |
| `long` | `padding_scheme` |  Padding to be used, the valid values are below: PKCS1.PADDING.RSA SSLV23.PADDING.RSA NO.PADDING.RSA PKCS1.OAEP.PADDING.RSA X931.PADDING.RSA DEFAULT.PADDING.RSA -> PKCS1.PADDING.RSA  |
| `ref string` | `output` |  base64 encoded encrypted string  |

## Return values
0 Success. -1 Error.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

	function void main()
	{
	        string public_key_file(512)
	        string data_in(512)
	        long data_in_len
	        string output(1024)
	        long ret
	        | The input string is the raw/binary string
	        data_in = "A user provided message"

	        | Length of the string. Care should be taken to specify the correct length
	        data_in_len=len.in.bytes(data_in)
	        public_key_file="/tmp/publickey.pem"
	        ret=rsa.encrypt(pub_key_file,data_in, data_in_len, PKCS1.PADDING.RSA,output)
	}
```
Notes
- This function is available in all TIV conditionally with the USE_RSA_ENCRYPT_FUNCTION compiler flag. The compiler flag can be defined as -D USE_RSA_ENCRYPT_FUNCTION.
