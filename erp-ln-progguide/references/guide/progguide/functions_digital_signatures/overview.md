# Digital Signatures overview
Digital Signatures enable verification of both authenticity and integrity of electronic documents. The user that signs a key has a key-pair with a private and public key. The private key is secret and can be used to encrypt data; the public key can be used to decrypt that data again. The public key is a certificate, signed by a certificate authority.
When signing a document, a fingerprint is created. This fingerprint is a unique hash - any change to the document will result in a different fingerprint. The fingerprint is encrypted using the private key and, together with the public key, embedded in the document. The recipient can verify integrity by using the embedded public key to decrypt the fingerprint. Calculating the fingerprint again on the received document will show whether it is modified or not. Because the public key is embedded in the document and signed by a certificate authority, the recipient can verify authenticity as well. Besides signing a document it is also possible to sign an individual string value.

## Signature request
To sign a document using the Digital Signatures API a sign request needs to be configured. The format determines the type of signature and depends on the type of document. The level specifies what additional information should be included in the signature. The packaging specifies how the data and signature should be combined (or not). For the PAdES format, only `ENVELOPED` is available. After setting the document, the output and the key information, the request can be executed.

## Related topics
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
