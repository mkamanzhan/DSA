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


def profile_solutions(solutions: list[Callable] | Callable, test_cases: list[TestCase]) -> None:
    # show in seconds like 0.0001
    if callable(solutions):
        solutions = [solutions]

    for solution in solutions:
        start = time.time()
        assert_solutions(solution, test_cases)
        end = time.time()
        print(f"{solution.__name__} took: {end - start:.4f} seconds")
