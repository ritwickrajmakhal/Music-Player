import unittest
import modules

class TestModulesMethods(unittest.TestCase):
    def test_setSongIndex(self):
        modules.setSongIndex(0)
        self.assertEqual(modules.askForSongIndexFile(),0)
    
    def test_setPos(self):
        modules.setPos(0)
        self.assertEqual(modules.askForPos(),0)

    def test_setPath(self):
        expected_path = modules.setPath()
        
        self.assertEqual(modules.askForPath(),expected_path)  
if __name__ == '__main__':
    unittest.main()