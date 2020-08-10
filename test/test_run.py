import unittest
import subprocess
import time


class Test(unittest.TestCase):

    def test_runcommand(self):

        result = subprocess.run('vimstartup')
        time.sleep(0.5)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
