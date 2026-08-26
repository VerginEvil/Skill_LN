# Cipher Functions overview
The Bshell provides access to cipher functions (encryption/decryption) of the OpenSSL library, which makes industry standard implementations of these cipher functions available to 3GL programs.
These functions are availabe as of [porting set TIV](../tiv/tiv_overview.md) [level 2000](../tiv/tiv_2000.md).
The provided ciphers are:
- CIPHER_AES_128_ECB
- CIPHER_AES_128_CBC
- CIPHER_AES_128_CFB1
- CIPHER_AES_128_CFB8
- CIPHER_AES_128_CFB128
- CIPHER_AES_128_OFB
- CIPHER_AES_128_CTR
- CIPHER_AES_128_XTS
- CIPHER_AES_192_ECB
- CIPHER_AES_192_CBC
- CIPHER_AES_192_CFB1
- CIPHER_AES_192_CFB8
- CIPHER_AES_192_CFB128
- CIPHER_AES_192_OFB
- CIPHER_AES_192_CTR
- CIPHER_AES_256_ECB
- CIPHER_AES_256_CBC
- CIPHER_AES_256_CFB1
- CIPHER_AES_256_CFB8
- CIPHER_AES_256_CFB128
- CIPHER_AES_256_OFB
- CIPHER_AES_256_CTR
- CIPHER_AES_256_XTS  Basically, this is AES (Advanced Encryption Standard) in 128, 192 and 256 bit blocks with various modes such as ECB (Electronic Code Book), CBC (Cipher Block Chaining), CFB (Cipher Feedback) and various others.
For each algorithm, there is an *initialize* function to select that algorithm for either an encryption or decryption operation, see [cipher.encrypt.initialize()](cipher.encrypt.initialize.md) and [cipher.decrypt.initialize()](cipher.decrypt.initialize.md).
After initialization, an *update* function is called to pass the data to encrypt or decrypt.
Lastly, a *finalize* function is called to retrieve the last (partial) block and to free the resources used by the operation.

## For example, to encrypt a bit of data:
```

 string input_buf(1024)
 string output_buf(1024)
 string tail(1024), answer(2048)
 string cipher_key(64)
 string iv(32)
 long id1, output_len, tail_len

 input_buf = "The text that needs to be encrypted, any length"
 hex_to_raw("67c7e4530f67a4112b678b737a82017f", cipher_key) | Create 16 bytes of key
 hex_to_raw("0123456789abcdef0123456789abcdef", iv) | Create Initialization Vector
 id1 = cipher.encrypt.initialize(CIPHER_AES_128_CFB1, cipher_key, iv)
 cipher.encrypt.update(id1, output_buf, output_len, input_buf))
 cipher.encrypt.finalize(id1, tail, tail_len))

 | append two binary strings to obtain the encrypted data
 copy.mem(answer, output_buf(1;output_len))
 copy.mem(answer(1 + output_len), tail(1;tail_len) )
 crylen = output_len + tail_len | Length of encrypted data
```
The cipher function requires that the key and initialization vector are passed as binary data. The hex_to_raw and raw_to_hex functions are used as example functions that translate between hexadecimal strings and binary data.
The *answer* string is the concatenation of the *output_buf* and the *tail*, this is because many cipher function can only operate on blocks of data of a certain internal block length. If the input data is not a multiple of that length, it is padded internally, but there can be a final partial block that is returned by the *finalize* function.
To decrypt data, the same key, initialization vector and ecrypted data is fed to the *decrypt* functions.

## Example:
```

function main ()
{
	string input_buf(1024)
	string output_buf(1024)
	string tail(1024), answer(2048)
	string cipher_key(64)
	string iv(32)
	long id1, output_len, tail_len, crylen

 	input_buf = "The Quick Brown Fox Jumps Over the Lazy Cat"

 	hex_to_raw("67c7e4530f67a4112b678b737a82017f", cipher_key) | Create 16 bytes of key
 	hex_to_raw("0123456789abcdef0123456789abcdef", iv) 	   | Create Initialization Vector
 	id1 = cipher.encrypt.initialize(CIPHER_AES_128_CFB1, cipher_key, iv)
 	cipher.encrypt.update(id1, output_buf, output_len, input_buf)
 	cipher.encrypt.finalize(id1, tail, tail_len)

 	| append two binary strings to obtain the encrypted data
	copy.mem(answer, output_buf(1;output_len))
	copy.mem(answer(1 + output_len), tail(1;tail_len) )
 	crylen = output_len + tail_len | Length of encrypted data

	long id2
	string decrypt_buf(2048)

	set.mem(output_buf,chr$(0),1024)
	set.mem(tail,chr$(0),1024)

	id2 = cipher.decrypt.initialize(CIPHER_AES_128_CFB1,cipher_key,iv)
	| Feed the encrypted data (in answer) and the proper length to the update function
	cipher.decrypt.update(id2, output_buf, output_len, answer, crylen)
	cipher.decrypt.finalize(id2, tail, tail_len)
	decrypt_buf = output_buf(1;output_len) & tail(1;tail_len)
	|*** decrypt_buf contains original "The Quick ... etc"
}

function void	hex_to_raw(const string	hex_string(),ref string	raw_string())
{
	long	hex_index
	long	raw_index

	hex_index	= len.in.bytes( hex_string )
	raw_index	= hex_index / 2

	while hex_index <> 0
		long	low_value
		long	high_value

		low_value	= pos("0123456789abcdef", hex_string(hex_index;1)) - 1
		hex_index	= hex_index - 1
		high_value	= pos("0123456789abcdef", hex_string(hex_index;1)) - 1
		hex_index	= hex_index - 1

		store.byte( 16 * high_value + low_value, raw_string(raw_index) )
		raw_index	= raw_index - 1
	endwhile
}
```
Note the set.mem() calls to clear buffers, which are required because the strings are treated as binary chunks of data by the cipher functions.

## Related topics
- [Cipher Function synopsis](cipher_synopsis.md)
- [Secure Digest Functions overview](../functions_digest/digest_overview.md)
