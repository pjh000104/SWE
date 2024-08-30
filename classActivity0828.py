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
    unittest.main()
