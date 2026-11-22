# Python notes

## Ch01: Data types
- Python's `float` is a 64-bit double; there's no separate `double` type.
- `int` has no size limit (`2 ** 1000` works).
- `0.1 + 0.2` gives `0.30000000000000004`, which is normal float behavior.
- For money, use `Decimal('0.1')` from the `decimal` module (exact).
