from test_framework import TestSuite
from test_framework_test import TestCaseTest, TestResult, TestSuiteTest

result = TestResult()
suite = TestSuite()

suite.add_test(TestCaseTest("test_result_success_run"))
suite.add_test(TestCaseTest("test_result_failure_run"))
suite.add_test(TestCaseTest("test_result_error_run"))
suite.add_test(TestCaseTest("test_result_multiple_run"))
suite.add_test(TestCaseTest("test_was_set_up"))
suite.add_test(TestCaseTest("test_was_run"))
suite.add_test(TestCaseTest("test_was_tear_down"))
suite.add_test(TestCaseTest("test_template_method"))

suite.add_test(TestSuiteTest("test_suite_size"))
suite.add_test(TestSuiteTest("test_suite_success_run"))
suite.add_test(TestSuiteTest("test_suite_multiple_run"))

suite.run(result)
print(result.summary())
