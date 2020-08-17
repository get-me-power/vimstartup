import unittest
import subprocess
import time


class Vim_Test(unittest.TestCase):

    def test_runcommand(self):
        result = subprocess.run('vimstartup')
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)

    def test_runhelp(self):
        result = subprocess.run(['vimstartup', '--help'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)

    def test_runversion(self):
        result = subprocess.run(['vimstartup', '--version'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
