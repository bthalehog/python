#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import re
import os
import sys
from unittest import TextTestRunner
from examiner.exam_test_case import ExamTestCase
from examiner.exam_test_result import ExamTestResult
from examiner.helper_functions import import_module
from examiner.helper_functions import find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)


class Test1PlaneStructure(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    def test_file_marvin_py_exist(self):
        """
        Testerna hittar inte filen 'marvin.py'.
        """
        self.tags = ["struct"]
        with patch("builtins.input", side_effect=''):
            with patch("sys.stdout", new=StringIO()) as _:
                try:
                    self.assertModule("plane", REPO_PATH)
                except StopIteration:
                    self.assertTrue(True)





if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
