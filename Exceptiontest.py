import unittest
from prime-numbers import prime_numbers
def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))

class ExceptionTest(unittest.TestCase):
    def test_trap_local(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see expected ValueError')
            
    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')
        
if __name__ == '__main__':
    unittest.main()


