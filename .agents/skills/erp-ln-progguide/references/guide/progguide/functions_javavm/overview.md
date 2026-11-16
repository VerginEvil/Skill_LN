# Java VM integration - Infor Enterprise Server 3GL

## Introduction
Starting from BaanERP 5.0c, java programs can be called from within the Infor Enterprise Server. The Java VM has been integrated within the Baan Virtual Machine (BaanVM, also known as the Bshell). This integration is also known as JVMI.
Using the JVMI, it is possible to:

- Start Java programs;

- Exchange messages (also known as buckets) between Java and Infor Enterprise Server.

Starting from Infor LN 10.4.1 it is also possible to load, execute and unload java programs dynamically. These functions allow the deployment of new versions of a Java program without disrupting running programs or the need to overwrite existing versions of software (which is not possible in Windows environments if the object is being used by a currently running program).
This dynamic system can be used next to the older system described below. For new applications the newer calls are preferred:

- [java.load.application](java.load.application.md)

- [java.execute.static.application.method](java.execute.static.application.method.md)

- [java.unload.application](java.unload.application.md)

## Overview
The JVMI consists of the following parts:

- Bucket. A bucket consists of a header (type is string) and a body. The body can contain any information you like.

- Queues (which are maintained within Infor Enterprise Server). These queues are used to store buckets. Buckets are stored and retrieved using the FIFO (first in first out) principle.

- Listeners. Whenever a new bucket arrives on a queue, the listener of that queue is notified. Zero or one listeners can be installed on a queue. A listener can be installed in Java, or in Infor Enterprise Server! Another advantage is that a listener decides what to do with a particular bucket. For example, one type of listener could route it 'as is' to another queue, while another listener could write that same bucket into the database.

- Methods to create/remove queues, send/retrieve buckets, and to install/remove listeners.

- Methods to start a Java program directly. Only static Java methods with return type void can be called (e.g. public static void startThisMethod()). The signature of the method (the parameters it receives) must match the call in 3GL. Strings, longs and arrays are supported.

The following figure shows an example of an application using JVMI:
In the picture above, Infor Enterprise Server sends buckets to Java, and Java sends the same buckets back to Infor Enterprise Server. It is implemented as follows (for more details please read the specific sections of this document):

- From Infor Enterprise Server, create two queues (using java.new.queue)

- On one queue, install a listener at the Infor Enterprise Server end (using java.install.listener). In the picture above, this listener is called BVM listener.

- Next, install a listener at the Java end by java.execute.static.method.async("java listener class name", "method name", queue_id). This will start a Java program, which will register itself as a listener on the Java queue. In the picture above, this is called the JVM listener.

- Place a message from Infor Enterprise Server on the outgoing Java queue (using java.put.bucket)

- The listener at the Java end is triggered through the onReceive() method (part of the Java listener interface).

- In this particular case, the message is placed without any modification on the queue to Infor Enterprise Server.

- The listener in Infor Enterprise Server is triggered. It generates an event (EVT_CHANNEL_EVENT).

- The Infor Enterprise Server program script receives the event (through the standard event handling functions), and retrieves the message using java.get.bucket.

## 3GL functions of the JVMI
- [java.execute.static.method.sync](java.execute.static.method.sync.md)

- [java.execute.static.method.async](java.execute.static.method.sync.md)

- [java.new.queue](java.new.queue.md)

- [java.destroy.queue](java.destroy.queue.md)

- [java.install.listener](java.install.listener.md)

- [java.uninstall.listener](java.uninstall.listener.md)

- [java.put.bucket](java.put.bucket.md)

- [java.get.bucket](java.get.bucket.md)

- [java.lookup.queue](java.lookup.queue.md)

- [java.load.application](java.load.application.md)

- [java.execute.static.application.method](java.execute.static.application.method.md)

- [java.unload.application](java.unload.application.md)

## Java Interfaces of the JVMI
