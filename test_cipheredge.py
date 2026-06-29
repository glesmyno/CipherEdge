# test_cipheredge.py
"""
Tests for CipherEdge module.
"""

import unittest
from cipheredge import CipherEdge

class TestCipherEdge(unittest.TestCase):
    """Test cases for CipherEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CipherEdge()
        self.assertIsInstance(instance, CipherEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CipherEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
