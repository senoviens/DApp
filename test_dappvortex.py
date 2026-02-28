# test_dappvortex.py
"""
Tests for DAppVortex module.
"""

import unittest
from dappvortex import DAppVortex

class TestDAppVortex(unittest.TestCase):
    """Test cases for DAppVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAppVortex()
        self.assertIsInstance(instance, DAppVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAppVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
