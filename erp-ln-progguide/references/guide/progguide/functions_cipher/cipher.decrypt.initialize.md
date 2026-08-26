# cipher.decrypt.initialize()

## Syntax:
`function long cipher.decrypt.initialize( long crypt.type, string key, string iv )`

## Description
Initializes the state of the Decrypt Algorithm and selects the appropriate decryption algorithm.

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
| `string` | `key` |  The key with which the data is to be decrypted. The key must be of the length required by the algorithm (usually at least 16 bytes). The format is raw binary. The key must have the *exact* same value as used during encryption.  |
| `string` | `iv` |  The initialization vector. This parameter is optional. When no initialization vector is given and the algorithm requires one, a default IV is used. When the data is decrypted, the *same* IV must be used. An IV is used as a starting vector for the feedback modes of the algorithm: the results of the previous block decryption are used as input for the next block decryption operation. The IV serves as input for the first such block. The IV must have the *exact* same value as used during encryption.  |

## Return values
A handle for this decrypt operation that must be used in subsequent calls to [cipher.decrypt.update()](cipher.decrypt.update.md) and [cipher.decrypt.finalize()](cipher.decrypt.finalize.md).
The returned *Id* can only be used in the original process where cipher.decrypt.initialize was called, and is useless in other processes in the same bshell.
The allocated memory is freed explicitly by passing the Id to cipher.decrypt.finalize(). The allocated memory is freed implicitly when the process exits.
Any number of Cipher Encrypt Algorithm ID's may be in use concurrently.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Cipher Functions overview](cipher_overview.md)
- [Cipher Function synopsis](cipher_synopsis.md)
