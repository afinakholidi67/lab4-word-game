def fib(n: int) -> int:
    """Return the n-th Fibonacci number using a simple recursive algorithm.

    This implementation is intentionally naive and exhibits exponential time
    complexity. It's suitable for small values of `n` and educational purposes.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # simple demonstration when the module is run directly
    import sys

    try:
        count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Usage: python main.py [n]")
        sys.exit(1)

    print(f"fib({count}) = {fib(count)}")
