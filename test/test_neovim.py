import unittest
import subprocess
import time


class Nvim_Test(unittest.TestCase):

    def test_runcommand(self):
        result = subprocess.run(['vimstartup', '--nvim'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)

    def test_run_clean(self):
        result = subprocess.run(['vimstartup', '--nvim', '--extra', '--clean'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)

    def test_fail(self):
        # not exist --noexist option, should test fail
        result = subprocess.run(['vimstartup', '--nvim', '--extra', '--noexist'])
        print('\n')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
