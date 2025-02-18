def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Division by zero")
        else:
            return a + b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or some other appropriate handling