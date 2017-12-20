import unittest

class TestMath(unittest.TestCase):
     #@unittest.skip("demonstrating skipping")
    def test_upper(self):
        add = lambda x, y: x + y
        self.assertEqual(4, add(2, 2))

    def test_rest(self):
        # define the rest function
        def add(*nums):
            sum = 0
            for num in nums:
                sum = sum + num
            return sum
        self.assertEqual(6, add(2, 2, 2), 'Math is Error!')

class TestFunction(unittest.TestCase):
    
    def test_dict(self):
        # define count
        def count(**nums):
            sum = nums["x"] + nums["y"]
            return sum
        self.assertEqual(5, count(x=2, y=3))

    def test_mix(self):
        def add(x,  y, *nums, **vs):
            sum = x + y
            for num in nums:
                sum = sum + num
            return sum + vs["a"] + vs["b"]
        self.assertEqual(15, add(1, 4, 2, 3, a=0, b=5))
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMath)
    suite.addTest(TestFunction)
    return suite
'''

if __name__ == '__main__':
    ''''''
    test_cases = (TestMath, TestFunction)
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    #unittest.main()
    
    #unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.TextTestRunner(verbosity=2).run(suite)
