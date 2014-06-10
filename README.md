
Java Datastream read and write in Python
========================================

This is a simple Python library for reading and writing Javas data stream format.

The file data_input_stream.py provides (almost) all of the methods defined in Javas [DataInputStream](http://docs.oracle.com/javase/7/docs/api/java/io/DataInputStream.html) for reading primitive Java data types from a input stream.

The file data_output_stream.py provides (almost) all of the methods defined in [DataOutputStream](http://docs.oracle.com/javase/7/docs/api/java/io/DataOutputStream.html) for writing to a Java output stream.

Example
-------

    with open('/tmp/stream', 'wb') as f:
        dos = DataOutputStream(f)
        dos.write_int(12345)
        dos.write_utf('hello world')

    with open('/tmp/stream', 'rb') as f:
        dis = DataInputStream(f)
        val = dis.read_int()
        string = dis.read_utf()


Tests
------

Simple unittests exists in file test.py
        
        
(You should note that the library has no exception handling and might not be accurate in the way it handles UTF-strings with NULL characters. For my use case it is working well but if you are planning on using the library for something important you should probably verify that everything works for you.)
