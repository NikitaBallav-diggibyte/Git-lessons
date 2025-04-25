import unittest, example
# import unittest
#
# Brings in Python’s built-in testing tool called unittest.
# This lets you write test cases and check if your code works correctly.

# import example
#
# This loads your own file named example.py, which has the function you want to test.
# So now you can use example.greet_person() in your test


class TestExample(unittest.TestCase):
# Here, you're creating a test class.
#
# TestExample is the name of your test class . You can name it anything, but it's common to start with Test....
#
# (unittest.TestCase) means you're saying:
# "Hey Python, this is a test case and I want to use all the tools from the unittest module."
# Basically, TestExample is inherited from the unittest.TestCase class
# So now, inside this class , you can write your test functions — like test_greet_person.
#
    def test_greet_person(self):
        greeting_message= example.greet_person("Joe")

        self.assertEqual(greeting_message, "Welcome Joe")

        self.assertEqual(example.greet_person("joe"), "Welcome Joe")

    def test_can_drink_alcohol(self):
        self.assertFalse(example.can_drink_alcohol(16))
        self.assertTrue(example.can_drink_alcohol(34))

if __name__=="__main__":
    print("__name__: ", __name__)
    unittest.main() # "Hey python, run all the tests in this file now"