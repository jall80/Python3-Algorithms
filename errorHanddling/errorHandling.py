def divide(a, b):
    # Validation with assert (only active in debug mode)
    assert isinstance(a, (int, float)), "Dividend must be a number."
    assert isinstance(b, (int, float)), "Divisor must be a number."

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def save_result(result, filename="results.txt"):
    try:
        with open(filename, "a") as f:
            f.write(f"Result: {result}\n")
    except Exception as e:
        print(f"⚠️ Could not save the result: {e}")

def main():
    print("🧮 Safe Division Calculator")
    a = get_number("Enter the dividend: ")
    b = get_number("Enter the divisor: ")

    try:
        result = divide(a, b)
    except ZeroDivisionError as e:
        print(f"🚫 Error: {e}")
    except AssertionError as e:
        print(f"🔍 Validation error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    else:
        print(f"✅ Result: {result}")
        save_result(result)
    finally:
        print("📝 Operation finished (success or error).")

if __name__ == "__main__":
    main()
