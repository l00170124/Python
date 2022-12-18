import unittest 
import formater 

class TestFormatter(unittest.TestCase): 
    def test_lower(self): 
        test_text = "JOHN ORAW" 
        result = formater.convert_lower(test_text) 
        self.assertEqual(result, "john oraw") 
        
    def test_upper(self): 
        test_text = "John ORaw" 
        result = formater.convert_upper(test_text) 
        self.assertEqual(result, "JOHN ORAW") 
        
    if __name__ =="__main":
        unittest.main()