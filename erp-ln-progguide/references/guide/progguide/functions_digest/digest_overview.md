# Secure Digest Functions overview
These functions are available as of [porting set TIV](../tiv/tiv_overview.md) [level 2000](../tiv/tiv_2000.md).
Digest (or hash) algorithms are meant to compute a condensed representation of a message or a data file. For an arbitrary length message, the algorithm produces a fixed-length output called a message-digest. These functions can be used to digitally sign data, as a minimal change in the input produces a significantly different output. The Bshell has provided the [Secure Hash Algorithm synopsis](../functions_sha/sha_synopsis.md) for many years, but those functions are superseded by the functions described here. They provide a simple, modern, consistent and extensible interface to the standard OpenSSL implementations of these digest algorithms.
Use them by calling the digest.initialize function, then feed the digest.update function the entire message (in as many parts as is convenient). The digest.finalize function then returns the resulting message digest.
The provided digest algorithms are:

- DIGEST_MD5

- DIGEST_SHA1

- DIGEST_SHA224

- DIGEST_SHA256

- DIGEST_SHA384

- DIGEST_SHA512

- DIGEST_SHA3_224

- DIGEST_SHA3_256

- DIGEST_SHA3_384

- DIGEST_SHA3_512

Note: the older DIGEST_SHA algorithm (also known as SHA-0) has been removed from the bshell version 9.1c, TIV 2140, as versions of OpenSSL starting with 1.1.0c do not support the SHA digest anymore. The SHA-0 algorithm has been considered insecure ever since 1995.
The same goes for DIGEST_MDC2, which is a DES2 based hash, and support for that has been removed from the bshell version 9.3e, TIV 2340.
DIGEST_SHA384 was added to the bshell in version 9.5b, TIV 2510.
If you use the DIGEST_SHA or DIGEST_MDC2 name, you will get a runtime error for compiled objects if this method is used and an intentional compilation error of 3GL objects when you try to compile a source containing it. You will have to alter your software to use one of the newer digest algorithms.
As an example:
```

long id
string result(100)

id = digest.initialize(DIGEST_MD5)
digest.update(id,"The quick brown fox jumps over ")
digest.update(id,"the lazy dog")
digest.finalize(id, result)	| Result is now "9E107D9D372BB6826BD81D3542A419D6"
```

## Related topics
- [Secure Digest Functions synopsis](digest_synopsis.md)
