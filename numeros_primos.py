import unittest

def is_primo(value):
    if value > 7:
        if value % 2 == 0 or value % 3 == 0 or value %5 == 0 or value %7 == 0:
            return False
        else: return True
    else:
        if value == 2 or value == 3 or value == 5 or value == 7:
            return True
        else:  
            return False
    


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_100(self):
        result = is_primo(6)
        self.assertEqual(result, False)   
    
    def test_15(self):
        result = is_primo(15)
        self.assertEqual(result, False)
   
    def test_113(self):
        result = is_primo(113)
        self.assertEqual(result, True)
    
    def test_127(self):
        result = is_primo(127)
        self.assertEqual(result, True)
    
    def test_114(self):
        result = is_primo(114)
        self.assertEqual(result, False)



unittest.main()