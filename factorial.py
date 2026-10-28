"""Calculate the factorial of a non-negative integer."""


def factorial_iterative(n: int) -> int:
    """Return n! using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Return n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main() -> None:
    raw = input("Enter a non-negative integer: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Please enter a valid integer.")
        return

    try:
        print(f"{number}! (loop)       = {factorial_iterative(number)}")
        print(f"{number}! (recursion)  = {factorial_recursive(number)}")
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
