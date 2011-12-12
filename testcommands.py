from cmdhelper import CommandOptions

__author__ = 'yan'

import unittest

class MyTestCase(unittest.TestCase):

    def test_1(self):
        pass
#        cmds = ("apache", "mysql")
#        opts = []
#
#        for cmd in cmds:
#            objCmdOpt = CommandOptions(cmd)
#            print cmd
#            opts = objCmdOpt.select_options()
#            self.assertEqual(len(opts), 4)

if __name__ == '__main__':
    unittest.main()
