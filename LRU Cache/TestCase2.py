import unittest
from LRUCache import LRUCache

class TestLRUCacheBasic(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)  

    def test_basic_operations(self):
        self.cache.put(1, 90)  
        self.cache.put(2, 80)
        self.cache.put(3, 70)
        self.assertEqual(self.cache.get(1), 90) 
        self.assertEqual(self.cache.get(2), 80) 

        # Test LRU eviction
        self.cache.put(4, 60)  
        self.assertEqual(self.cache.get(3), -1)  
        self.assertEqual(self.cache.get(4), 60) 

        self.cache.put(2, 50)  
        self.assertEqual(self.cache.get(2), 50) 
        self.assertEqual(self.cache.get(1), 90)  

if __name__ == "__main__":
    unittest.main()
