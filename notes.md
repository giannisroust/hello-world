# Python notes

## Ch01: Data types
- Python's `float` is a 64-bit double; there's no separate `double` type.
- `int` has no size limit (`2 ** 1000` works).
- `0.1 + 0.2` gives `0.30000000000000004`, which is normal float behavior.
- For money, use `Decimal('0.1')` from the `decimal` module (exact).


## Ch04: try / except (handling errors)

- `try:` runs code that *might* fail; `except SomeError:` runs only if that error happens.
  Without it, an error crashes the program with a traceback.
- Catch **specific** errors (`except ValueError:`), not a bare `except:`.
  A bare `except` also swallows bugs and even Ctrl+C, which hides real problems.
- `KeyboardInterrupt` is the "error" raised when you press **Ctrl+C**.
  Catching it lets a program stop cleanly instead of printing a traceback
  (used in spike.py: endless animation, Ctrl+C → `sys.exit()`).
- Common pattern: validate user input
    ```python
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Please enter a number.")
    ```
- Optional extras (later): `else:` runs if no error happened,
  `finally:` always runs (e.g. to close a file).

## Lists: negative indexes

- `ages[-1]` = last item, `ages[-2]` = second to last, etc.
  No need to know the list's length.
- `ages[0]` = first item.
- Square brackets `[ ]` = get an item; round brackets `( )` = call a function.
  `ages(-1)` → TypeError: 'list' object is not callable.

## assert (sanity checks)

- `assert condition` → if True, nothing happens; if False, the program stops
  with `AssertionError`.
    ```python
    ages.sort()
    assert ages[0] <= ages[-1]  # sorted list: first <= last
    ```
- Use it to catch **my own bugs** early ("this should never happen").
- Don't use it to check user input; use `if` or `try/except` for that.
  (Python can be run with asserts switched off.)
- pytest tests are basically asserts: `assert decide_winner("r", "s") == "win"`