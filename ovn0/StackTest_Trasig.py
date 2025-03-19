import unittest

import stack as StackClass #Modul som innehåller klassen som vi ska testa

class Test(unittest.TestCase): #Vi ärver från TestCase för att komma åt funktionaliteten
    
    #Vi ska inte ha en init-metod i den här klassen. Om vi har det får fel inifrån unittestmodulen:
    # TypeError: Test.__init__() takes 1 positional argument but 2 were given 
    def __init__(self):
        self.stack = StackClass.Stack()

    def test_0push(self): 
        """Testar att tillägg av element ökar längden"""
        self.stack.push(" world!")
        self.assertEqual(len(self.stack), 1)
        self.stack.push("Hello,")
        self.assertEqual(len(self.stack), 2)
    

if __name__=='__main__':
    unittest.main()