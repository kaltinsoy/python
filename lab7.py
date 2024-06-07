import re
def is_valid_float(N):
    # Define the regex pattern for a valid floating point number
    pattern = r'^[+-]?[0-9]*\.?[0-9]*$'
    # Check if N matches the pattern
    if re.match(pattern, N.strip()):
    # Try converting N to a float and catch any exceptions
        try:
            float(N)
            return True
        except ValueError:
            return False
        except Exception:
            return False
    else:
        return False
# Test the function
test_cases = ["+6.9","-1.0",".7","+.5","-.819","-+8.7","11.","11.0","4.0O0","nothing","15.29"]
for case in test_cases:
    print(f"{case}: {is_valid_float(case)}")