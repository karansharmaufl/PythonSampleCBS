import unittest
from HelloWorld import HelloWorld

class TestCase(unittest.TestCase):
    def test_hello_msg(self):
        hw = HelloWorld()
        self.assertEqual(hw.message, 'Heavy Water!')

if __name__ == '__main__':
    unittest.main()