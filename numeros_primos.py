import unittest

def is_primo(value):
    div = 2
    while div < value:
        if value % div == 0:
            return False
        div += 1
    return True


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result,True)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result,True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result,True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result,False)

unittest.main()