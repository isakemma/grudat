import unittest

from stack import Stack  #Klass som vi ska testa

class Test(unittest.TestCase): #Vi ärver från TestCase för att komma åt funktionaliteten

    def setUp(self):
        self.stack = Stack()
        return super().setUp()

    def test_0push(self): 
        """Testar att tillägg av element ökar längden"""
        self.stack.push(" world!")
        self.assertEqual(len(self.stack), 1)
        self.stack.push("Hello,")
        self.assertEqual(len(self.stack), 2)
    
    def test_1pop(self):
        """Testar att utplockning av elementen sker i omvänd ordning och att stacken töms"""
        self.stack.push(" world!")
        self.stack.push("Hello,")
        res = ""
        exp = "Hello, world!"
        while len(self.stack) > 0:
            res += self.stack.pop()
        self.assertEqual(res, exp)
        self.assertTrue(len(self.stack)==0)
        
    
    def test_2popEmpty(self):
        """Testar att vi får IndexError när vi anropar pop på en tom stack"""
        with self.assertRaises(IndexError):
            self.stack.pop()

if __name__=='__main__':
    unittest.main()