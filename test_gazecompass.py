# test_gazecompass.py
"""
Tests for GazeCompass module.
"""

import unittest
from gazecompass import GazeCompass

class TestGazeCompass(unittest.TestCase):
    """Test cases for GazeCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GazeCompass()
        self.assertIsInstance(instance, GazeCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GazeCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
