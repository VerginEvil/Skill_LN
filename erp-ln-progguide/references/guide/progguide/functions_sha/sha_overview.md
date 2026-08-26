# Secure Hash Algorithm overview
NOTE: These functions are superseded by the more general [Secure Digest Functions overview](../functions_digest/digest_overview.md), available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) 2000.
The Secure Hash Algorithm SHA-1 is a standard algorithm meant to compute a condensed representation of a message or a data file. For an arbitrary length message, the algorithm produces a 160-bit output called a message-digest. See FIPS 180-1 - Secure Hash Standard for a complete description of the standard. The standard limits the message size to any value less than 2^64 bits. The implementation described here limits the message size to 2^41 bits, in multiples of 8 bits, i.e. any amount of bytes less than 2^38 bytes (256 GigaByte).

## Related topics
- [Secure Hash Algorithm synopsis](sha_synopsis.md)
