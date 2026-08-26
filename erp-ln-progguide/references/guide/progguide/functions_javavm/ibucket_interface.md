# IBucket Interface
With the IBucket interface, it is possible to modify the bucket and to read the contents of a bucket. The interface is instantiated using the createBucket method of the IBaanVM interface.

## Interface methods
`public String getHeader();`
Retrieves the header of the bucket, in String format.
`public void setHeader(String p_hdr);`
Sets the header of the bucket. P_hdr becomes the new header.
`public byte[] getBucket();`
Retrieves the message within the bucket as a byte array.
`public String toString();`
Retrieves the message within the bucket in String format.
`public void setBucket(String p_msg); public void setBucket(byte[] p_msg);`
Sets the message within the bucket. The contents of the message will be set using the content of p_msg.
