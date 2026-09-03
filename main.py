from test_framework import MyTest, TestResult

result = TestResult()

test = MyTest("test_a")
test.run(result)

test = MyTest("test_b")
test.run(result)

test = MyTest("test_c")
test.run(result)

print(result.summary())
