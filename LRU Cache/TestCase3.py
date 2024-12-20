import unittest
from LRUCache import LRUCache

class TestLRUCacheAdvanced(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(5)  

    def test_advanced_features(self):
        for i in range(1, 6):
            self.cache.put(i, i * 10)
        
        # Ensure all items are accessible
        for i in range(1, 6):
            self.assertEqual(self.cache.get(i), i * 10)
        
        # Test resizing the cache
        self.cache.resize(3)  
        self.assertEqual(len(self.cache._cache), 3) 

        # Check if the least recently used items were evicted
        self.assertEqual(self.cache.get(1), -1)  
        self.assertEqual(self.cache.get(2), -1)  

        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.cache.put(-1, 50) 
        with self.assertRaises(ValueError):
            self.cache.put(1, -50)  
        with self.assertRaises(ValueError):
            self.cache.resize(0) 

if __name__ == "__main__":
    unittest.main()
