
import os
import unittest
from data_input_stream import DataInputStream
from data_output_stream import DataOutputStream


class TestInputOutput(unittest.TestCase):

    def tearDown(self):
        os.system('rm testdata.tmp')
        
    def test(self):
        with open('testdata', 'rb') as f:
            dis = DataInputStream(f)
            self.assertEqual(dis.read_utf(), 'g\xc3\xb6teborg')
            self.assertEqual(dis.read_long(), 1349263067)
            self.assertEqual(dis.read_long(), -1349263067)
            self.assertEqual(dis.read_int(), 439)
            self.assertEqual(dis.read_boolean(), True)
            self.assertEqual(dis.read_boolean(), False)
            self.assertAlmostEqual(dis.read_float(), 123.456, 3)
            self.assertEqual(dis.read_double(), 123456.789)
            self.assertEqual(dis.read_char(), 'a')
            self.assertEqual(dis.read_byte(), 97)
            self.assertEqual(dis.read_unsigned_byte(), 97)
            self.assertEqual(dis.read_short(), -100)
            self.assertEqual(dis.read_short(), 100)

        with open('testdata.tmp', 'wb') as f:
            dos = DataOutputStream(f)
            dos.write_utf('g\xc3\xb6teborg')
            dos.write_long(1349263067)
            dos.write_long(-1349263067)
            dos.write_int(439)
            dos.write_boolean(True)
            dos.write_boolean(False)
            dos.write_float(123.456)
            dos.write_double(123456.789)
            dos.write_char('a')
            dos.write_byte(97)
            dos.write_unsigned_byte(97)
            dos.write_short(-100)
            dos.write_unsigned_short(100)

        with open('testdata', 'rb') as f:
            dis = DataInputStream(f)
            with open('testdata.tmp', 'rb') as f2:
                dis2 = DataInputStream(f2)
                self.assertEqual(dis.read_utf(), dis2.read_utf())
                self.assertEqual(dis.read_long(), dis2.read_long())
                self.assertEqual(dis.read_long(), dis2.read_long())
                self.assertEqual(dis.read_int(), dis2.read_int())
                self.assertEqual(dis.read_boolean(), dis2.read_boolean())
                self.assertEqual(dis.read_boolean(), dis2.read_boolean())
                self.assertEqual(dis.read_float(), dis2.read_float())
                self.assertEqual(dis.read_double(), dis2.read_double())
                self.assertEqual(dis.read_char(), dis2.read_char())
                self.assertEqual(dis.read_byte(), dis2.read_byte())
                self.assertEqual(dis.read_unsigned_byte(),
                                 dis2.read_unsigned_byte())
                self.assertEqual(dis.read_short(), dis2.read_short())
                self.assertEqual(dis.read_short(), dis2.read_short())                

if __name__ == '__main__':
    unittest.main()
