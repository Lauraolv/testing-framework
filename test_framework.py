class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def assert_equal(self, first, second):
        if first != second:
            msg = f"{first} != {second}"
            raise AssertionError(msg)

    def assert_true(self, expr):
        if not expr:
            msg = f"{expr} is not true"
            raise AssertionError(msg)

    def assert_false(self, expr):
        if expr:
            msg = f"{expr} is not false"
            raise AssertionError(msg)

    def assert_in(self, member, container):
        if member not in container:
            msg = f"{member} not found in {container}"
            raise AssertionError(msg)


class MyTest(TestCase):

    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")


class TestResult:

    RUN_MSG = "run"
    FAILURE_MSG = "failed"
    ERROR_MSG = "error"

    def __init__(self, suite_name=None):
        self.run_count = 0
        self.failures = []
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def add_failure(self, test):
        self.failures.append(test)

    def add_error(self, test):
        self.errors.append(test)

    def summary(self):
        return (
            f"{self.run_count} {self.RUN_MSG}, "
            f"{str(len(self.failures))} {self.FAILURE_MSG}, "
            f"{str(len(self.errors))} {self.ERROR_MSG}"
        )


class TestStub(TestCase):

    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception


class TestSpy(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"


class TestSuite:

    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestLoader:

    TEST_METHOD_PREFIX = "test"

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        test_method_names = list(
            filter(lambda method: method.startswith(self.TEST_METHOD_PREFIX), methods)
        )
        return test_method_names

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for test_method_name in self.get_test_case_names(test_case_class):
            test_method = test_case_class(test_method_name)
            suite.add_test(test_method)
        return suite


class TestRunner:

    def __init__(self):
        self.result = TestResult()

    def run(self, test):
        test.run(self.result)
        print(self.result.summary())
        return self.result
