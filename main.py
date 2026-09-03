from test_framework import TestLoader, TestRunner
from test_framework_test import TestLoader, TestLoaderTest, TestResult

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)
