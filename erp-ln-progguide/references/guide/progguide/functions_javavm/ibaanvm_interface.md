# IBaanVM interface
This is the main interface at the Java side. With this interface it is possible to create new buckets, place these buckets onto a queue, install a listener at the Java side (see IQueueListener description), and to log a message to the Bshell log file (handy for debugging purposes!).
Instantiating the interface can be done as follows:
`private static com.baan.baanvm.IBaanVM s_iBaanVm = null; s_iBaanVm = new com.baan.baanvm.BaanVMImpl();`

## Interface methods
`public IBucket createBucket(); public IBucket createBucket(String p_msg); public IBucket createBucket(byte[] p_msg); public IBucket createBucket(String p_msg, String p_hdr); public IBucket createBucket(byte[] p_msg, String p_hdr);`
Creates a new bucket. It is optional to specify a message (parameter p_msg) or a header (the p_hdr parameter). The new bucket can be manipulated using the IBucket interface. If the bucket is ready to be send, the function putBucket of the IBaanVM interface can be used to place the bucket onto a queue.
`public int putBucket(int p_queueId, IBucket p_bucket);`
Places a bucket (referenced by p_bucket) onto a queue (specified by p_queueId).
The return value is
| | |
|---|---|
| 0 | upon success |
| -1 | incorrect queue ID |
| < -1 | invalid bucket, or internal memory overflow |
`public void installListener(int p_queueId, IQueueListener p_listener) throws Exception;`
Installs a listener (at the Java side) on a queue. p_queueID is the ID of a queue which was previously created within Infor Enterprise Server. p_listener is an instance of a custom listener, which implements the IQueueListener interface. An exception is thrown in the following scenarios:
- the specified queue ID is invalid
- a listener is already installed on this queue  `public void logMessage(String p_message, int p_error);`
Writes a message to the logfile. p_message is the message to log. If p_error is greater than 0, the message is always written to the logfile. If p_error is 0, the message is only written in debug mode.
The logfile and debug mode can be toggled through the BW configuration options. The grammar for these options are:
-- keeplog -logfile <logfilename> [-dbgjvmi]
For example, the following line specifies a logfile and enables debugging. All calls to LogMessage will be placed in the logfile:
-- keeplog -logfile /home/gstam/jvmilogging.txt -dbgjvmi
To log calls to LogMessage, where p_error is greater than 0, use the following command:
-- keeplog -logfile /home/gstam/jvmilogging.txt
