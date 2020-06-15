import os
import sys
import unittest

wd = os.getcwd()
sys.path.append(f'{wd}/app')

from tests.unittests import test_prepare_task_data, test_model

tests2run = [
    test_prepare_task_data,
    test_model
]


def make_test_suite():
    import unittest

    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for test in tests2run:
        suite.addTest(loader.loadTestsFromModule(test))
    return suite


def run_tests():
    suite = make_test_suite()
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(result.failures) > 0 or len(result.errors) > 0:
        exit(1)


if __name__ == '__main__':
    run_tests()
