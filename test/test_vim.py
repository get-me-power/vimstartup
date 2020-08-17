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

    def test_run_noplugin(self):
        result = subprocess.run(['vimstartup', '--extra', '--noplugin'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)

    def test_fail(self):
        # not exist --nocommand option, should test fail
        result = subprocess.run(['vimstartup', '--extra', '--nocommand'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
