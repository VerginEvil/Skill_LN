# cipher.encrypt.initialize()

## Syntax:
`function long cipher.encrypt.initialize( long crypt.type, const string key, const string iv )`

## Description
Initializes the state of the Encryption Algorithm and selects the appropriate encryption algorithm.

## Arguments
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
| | | |
|---|---|---|
| `long` | `crypt.type` |  The name of the cipher algorithm. This must be one of the following: CIPHER_AES_128_ECB CIPHER_AES_128_CBC CIPHER_AES_128_CFB1 CIPHER_AES_128_CFB8 CIPHER_AES_128_CFB128 CIPHER_AES_128_OFB CIPHER_AES_128_CTR CIPHER_AES_128_XTS CIPHER_AES_192_ECB CIPHER_AES_192_CBC CIPHER_AES_192_CFB1 CIPHER_AES_192_CFB8 CIPHER_AES_192_CFB128 CIPHER_AES_192_OFB CIPHER_AES_192_CTR CIPHER_AES_256_ECB CIPHER_AES_256_CBC CIPHER_AES_256_CFB1 CIPHER_AES_256_CFB8 CIPHER_AES_256_CFB128 CIPHER_AES_256_OFB CIPHER_AES_256_CTR CIPHER_AES_256_XTS  |
| `const string` | `key` |  The key with which the data is to be encrypted. The key must be of the length required by the cipher algorithm (usually at least 16 bytes). The format is raw binary.  |
| `const string` | `iv` |  The initialization vector. This parameter is optional. When no initialization vector is given and the algorithm requires one, a default IV is used. When the data is decrypted, the *same* IV must be used. An IV is used as a starting vector for the feedback modes of the algorithm: the results of the previous block encryption are used as input for the next block encryption operation. The IV serves as input for the first such block.  |

## Return values
A handle for this encrypt operation that must be used in subsequent calls to [cipher.encrypt.update()](cipher.encrypt.update.md) and [cipher.encrypt.finalize()](cipher.encrypt.finalize.md).
The returned *Id* can only be used in the original process where cipher.encrypt.initialize was called, and is useless in other processes in the same bshell.
The allocated memory is freed explicitly by passing the Id to cipher.encrypt.finalize(). The allocated memory is freed implicitly when the process exits.
Any number of Cipher Encrypt Algorithm ID's may be in use concurrently.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Cipher Functions overview](cipher_overview.md)
- [Cipher Function synopsis](cipher_synopsis.md)
