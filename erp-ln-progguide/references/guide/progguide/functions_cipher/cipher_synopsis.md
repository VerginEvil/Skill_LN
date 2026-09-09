# Cipher Function synopsis
These functions are availabe as of [porting set TIV](../tiv/tiv_overview.md) [level 2000](../tiv/tiv_2000.md).
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [cipher.encrypt.initialize](cipher.encrypt.initialize.md) | `(long crypt.type,const string key,[const string iv])` |
|  | [cipher.encrypt.update](cipher.encrypt.update.md) | `(long handle, ref string data.out, ref long data.out.size, const string data.in, [long data.size.in.size ])` |
|  | [cipher.encrypt.finalize](cipher.encrypt.finalize.md) | `(long handle, ref string data.out, long data.out.size)` |
|  | [cipher.decrypt.initialize](cipher.decrypt.initialize.md) | `(long crypt.type,const string key,[const string iv])` |
|  | [cipher.decrypt.update](cipher.decrypt.update.md) | `(long handle, ref string data.out, ref long data.out.size, const string data.in, [long data.size.in.size ])` |
|  | [cipher.decrypt.finalize](cipher.decrypt.finalize.md) | `(long handle, ref string data.out, long data.out.size)` |
|  | [is_kms_encrypted](is_kms_encrypted.md) | `(string encrypted_password)` |

## Related topics
- [Cipher Functions overview](cipher_overview.md)

- [Secure Digest Functions overview](../functions_digest/digest_overview.md)

- [Secure Hash Algorithm overview](../functions_sha/sha_overview.md)
