"""
Shared test harness for all chapters.
Skycak uses the same test loop pattern throughout the book — defined once here.

Usage:
    from utils.test_runner import run_tests

    tests = [
        {'function': my_func, 'input': some_input, 'output': expected_output},
        ...
    ]
    run_tests(tests)

For functions that take multiple arguments, pass input as a tuple:
    {'function': add, 'input': (2, 3), 'output': 5}
"""


def run_tests(tests: list[dict]) -> None:
    num_successes = 0
    num_failures = 0

    for test in tests:
        function = test['function']
        test_input = test['input']
        desired_output = test['output']

        # Support single args or multi-arg tuples
        if isinstance(test_input, tuple) and test.get('unpack', True):
            actual_output = function(*test_input)
        else:
            actual_output = function(test_input)

        if actual_output == desired_output:
            num_successes += 1
        else:
            num_failures += 1
            function_name = function.__name__
            print(f'\n{function_name} failed on input {test_input!r}')
            print(f'\tActual output:  {actual_output!r}')
            print(f'\tDesired output: {desired_output!r}')

    status = "✓ All passed" if num_failures == 0 else f"✗ {num_failures} failed"
    print(f'\nTesting complete: {num_successes} successes, {num_failures} failures.  {status}')
