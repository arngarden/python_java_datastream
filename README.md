
Java Datastream read and write in Python
========================================

This is a simple Python library for reading and writing Javas data stream format.

The file data_input_stream.py provides (almost) all of the methods defined in Javas [DataInputStream](http://docs.oracle.com/javase/7/docs/api/java/io/DataInputStream.html) for reading primitive Java data types from a input stream.

The file data_output_stream.py provides (almost) all of the methods defined in [DataOutputStream](http://docs.oracle.com/javase/7/docs/api/java/io/DataOutputStream.html) for writing to a Java output stream.

Example
-------

    with open('/tmp/stream', 'wb') as f:
        dos = DataOutputStream(f)
        dos.write_long(12345678)
        dos.write_utf('hello world')

    with open('/tmp/stream', 'rb') as f:
        dis = DataInputStream(f)
        val = dis.read_long()
        string = dis.read_utf()

        