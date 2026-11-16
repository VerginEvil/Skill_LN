# IQueueListener Interface
This interface needs to be implemented by the developer which wants to exchange buckets between Java and Infor Enterprise Server. A listener needs to be installed using the IBaanVM.installListener() method.

## Interface methods
`public void onReceive(IBucket p_bucket);`
Whenever a bucket arrives on a queue for which the listener is installed, this method is called in a new Thread. p_bucket is the new message which has been received. It is up to the Java class that implements this interface what to do with the bucket
