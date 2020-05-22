import unittest
import hello_you

class TestHelloYou(unittest.TestCase):
    def test_hello_you(self):
        guid1 = hello_you.new_guid()
        guid2 = hello_you.new_guid()
        self.assertNotEqual(guid1, guid2)

if __name__ == '__main__':
    unittest.main()