from biba import BIBA
import unittest

mode = "strict"
data = ['1','a','sasd']
data1 = [1,2,4]
data2 = "test"
biba_1 = BIBA(1,data1,mode)
biba_1_1 = BIBA(11,data2,mode)
biba_2 = BIBA(2,data,mode)
biba_3 = BIBA(3,data,mode)
biba_4 = BIBA(4,data,mode)
biba_5 = BIBA(5,data1,mode)
class TEST(unittest.TestCase):
  def testWrite(self):
    biba_5.write(biba_1)
    assert biba_1.data == biba_5.data
    with self.assertRaises(Exception):
        biba_1.write(biba_5)
  def testRead(self):
    if mode=="cycle":
        biba_2.read(biba_1)
        biba_3.read(biba_4)
    elif mode=="low":
        biba_2.read(biba_1)
        assert biba_2.integrity == biba_1.integrity
    else:
        with self.assertRaises(Exception):
            biba_4.read(biba_3)
        biba_3.read(biba_5)
        biba_1.read(biba_1_1)

unittest.main()
