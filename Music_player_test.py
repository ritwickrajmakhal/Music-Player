import os
from time import sleep
import unittest
import modules
import Music_player as mp
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
    
    def test_nextSong(self):
        expected_songIndex = modules.askForSongIndexFile()
        expected_pos = modules.askForPos()
        mp.nextSong()
    
if __name__ == '__main__':
    unittest.main()