import unittest


class myClass:
    def myMethod(self, x):
        return x+5


class myChildClass(myClass):
    pass

# assert myclass.myMethod(2)>=10, "parameter is less than 5"
# assert myChildClass.myMethod(2)>=10, "parameter is less than 5"


class UnitTest(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        myclass = myClass()
        myclass2 = myChildClass()
        self.assertEqual(myclass.myMethod(2),7)
        self.assertLessEqual(5, myclass2.myMethod(5))


if __name__ == '__main__':
    unittest.main();

def is_palindrome(s: str) -> bool:
     cleaned = ''.join(char.lower() for char in s if char.isalnum())
     return cleaned == cleaned[::-1];
def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama!") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("No 'x' in Nixon") == True

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1);
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers"

test_factorial()