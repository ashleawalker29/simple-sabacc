import unittest

class HelloWorld:

    def __init__(self):
        self.message = 'Hello world!'

class HelloWorldTests(unittest.TestCase):

    def test_hello_world(self):
        hello_world = HelloWorld()
        self.assertEqual(hello_world.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()
