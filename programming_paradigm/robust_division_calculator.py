#!/bin/bash
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:  # Just in case, although float(denominator) == 0 should already catch this.
        return "Error: Cannot divide by zero."

if __name__ == "__main__":
    # This part will not execute when imported, only when run directly
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))
    print(safe_divide('ten', 5))
