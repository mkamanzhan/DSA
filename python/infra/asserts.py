from typing import Any, Callable, NamedTuple, Generic, TypeVar
import time


T = TypeVar("T")

class TestCase(NamedTuple, Generic[T]):
    params: T
    expected: Any


def assert_solutions(
    solutions: list[Callable] | Callable,
    test_cases: list[TestCase],
) -> None:
    if callable(solutions):
        solutions = [solutions]

    for solution in solutions:
        for test_case in test_cases:
            result = solution(**test_case.params._asdict())
            if result != test_case.expected:
                message = (
                    f"Failed for {solution.__name__} "
                    f"with {test_case.params}. "
                    f"Expected: {test_case.expected}, got: {result}"
                )
                print(message)


def _print_time(elapsed: float) -> str:
    if elapsed < 1e-6:
        return f"{elapsed * 1e9:.3f} nanoseconds"
    elif elapsed < 1e-3:
        return f"{elapsed * 1e6:.3f} microseconds"
    elif elapsed < 1:
        return f"{elapsed * 1e3:.3f} milliseconds"
    else:
        return f"{elapsed:.3f} seconds"


def profile_solutions(solutions: list[Callable] | Callable, test_cases: list[TestCase]) -> None:
    # show in human readable format: 0.001 seconds or 0.001 milliseconds or 0.001 microseconds or 0.001 nanoseconds
    if callable(solutions):
        solutions = [solutions]

    for solution in solutions:
        start = time.time()
        assert_solutions(solution, test_cases)
        end = time.time()
        elapsed = end - start
        print(f"{solution.__name__} took {_print_time(elapsed)}")
