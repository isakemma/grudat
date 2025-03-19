import unittest

from stack import Stack  #Klass som vi ska testa

class Test(unittest.TestCase): #Vi ärver från TestCase för att komma åt funktionaliteten

    def test_0push(self): 
        """Testar att tillägg av element ökar längden"""
        stack = Stack()
        stack.push(" world!")
        self.assertEqual(len(stack), 1)
        stack.push("Hello,")
        self.assertEqual(len(stack), 2)
    
    def test_1pop(self):
        """Testar att utplockning av elementen sker i omvänd ordning och att stacken töms"""
        stack = Stack()
        stack.push(" world!")
        stack.push("Hello,")
        res = ""
        exp = "Hello, world!"
        while len(stack) > 0:
            res += stack.pop()
        self.assertEqual(res, exp)
        self.assertTrue(len(stack)==0)
        
    
    def test_2popEmpty(self):
        """Testar att vi får IndexError när vi anropar pop på en tom stack"""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

if __name__=='__main__':
    unittest.main()