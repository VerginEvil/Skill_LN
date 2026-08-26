# hmac.hash()

## Syntax:
`function long hmac.hash( long type, const string key, long keysize, const string data, long size, ref string hash )`

## Description
Calculates a keyed-hash message authentication code (HMAC) using a cryptographic hash function in combination with a secret cryptographic key.
The cryptographic strength of the HMAC depends upon the cryptographic strength of the underlying hash function, the size of its hash output, and on the size and quality of the key.
The hash is returned in 'raw hex' format; depending on the specified hash type, this is a string of max 128 bytes.
The following cryptographic hash functions are supported:
- MD5
- SHA1
- SHA224
- SHA256
- SHA512

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  the hash function to use; one of: DIGEST_MD5, DIGEST_SHA1, DIGEST_SHA224, DIGEST_SHA256, DIGEST_SHA512  |
| `const string` | `key` |  the key to hash with  |
| `long` | `keysize` |  the size of the key in bytes; if -1 is specified, the size of the passed variable or string expression is used  |
| `const string` | `data` |  the data to return a hash for  |
| `long` | `size` |  the size of the data in bytes; if -1 is specified, the size of the passed variable or string expression is used  |
| `ref string` | `hash` |  the returned hash (a string of max 128 hex characters)  |

## Return values
| | |
|---|---|
| >= 0 | the number of hex characters copied into 'hash'; this is at max 128 |
| < 0 | in case of an error |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

string  key(32)
string  raw.data(1024)
string  hex.hash(128)
long    hex.hash.len
string  raw.hash(64)
long    raw.hash.len

|* assume key and raw.data have been assigned the correct values

|* calculate HMAC-SHA512 hash
hex.hash.len = hmac.hash(DIGEST_SHA512, key, 32, raw.data, 1024, hex.hash)

|* the hash contains HEX characters, convert to raw bytes if required
raw.hash.len = hex2bytes(hex.hash(1;hex.hash.len), raw.hash)
```

## Preconditions
- parameter 'type' must be one of: DIGEST_MD5, DIGEST_SHA1, DIGEST_SHA224, DIGEST_SHA256, DIGEST_SHA512

## Related topics
- [hex2bytes()](../functions_string_operations/hex2bytes.md)
- [Security Functions overview](security_overview.md)
- [Secure Functions synopsis](security_synopsis.md)
