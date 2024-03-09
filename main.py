from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    is an attempt to retrieve JSON-formatted user input, which upon success, returns
    that input as a list of numbers, or otherwise returns `None`.

    Returns:
        int: a list of numbers if the JSON input contains a valid `numbers` field,
        otherwise it returns `None`.

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes a list of integers as input, calculates their squares and returns them.

    Args:
        numbers (list): 1-dimensional array of integer values that are being
            processed, and it is used to generate a list of squares of those values.

    Returns:
        int: a list of square numbers.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes an iterable of numbers as input and returns a JSON response with either
    the squared values or an error message if no numbers were provided.

    Args:
        squared_numbers (list): 2D array or list of numbers to be squared and
            returned as JSON object in the function `display_result`.

    Returns:
        `HTTPResponse` object of status code `200`.: a JSON response with an error
        message if no numbers are provided.
        
        		- `squared_numbers`: A list of numbers provided as input to the function,
        which are then squared.
        		- `status_code`: The HTTP status code of 200 or 400 depending on whether
        the function successfully executed and provided output.
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    receives a list of numbers from the user, squares them using the `process_input`
    function, and returns the squared values to the user via the `display_result`
    function.

    Returns:
        list: the list of squared numbers computed from user input.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

def two_sum(nums, target):
    """
    takes a list of numbers and a target value as input, maps each number to its
    index in the list, and returns a list of indices representing pairs of
    corresponding values that add up to the target value.

    Args:
        nums (list): 1D array of integers that is searched for pairs whose sum is
            equal to the `target` parameter.
        target (int): 2-sum problem goal, which is the value to be found among the
            given numbers for each position in the list of numbers.

    Returns:
        list: a list of index-value pairs where each index corresponds to a number
        in the `nums` list and each value is the complement of that number.

    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

def reverse_integer(x):
    """
    computes the reciprocal of an integer by iteratively dividing it by 10 and
    storing the digits in a running total, signing the result based on the original
    value's sign.

    Args:
        x (int): 32-bit signed integer to be reversed.

    Returns:
        int: a positive or negative integer, representing the reverse of an input
        integer value.

    """
    sign = 1 if x >= 0 else -1
    x = abs(x)
    reversed_x = 0
    while x != 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    reversed_x *= sign
    return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0

def is_palindrome(x):
    """
    checks if a given number is a palindrome by recursively calculating its reverse
    and comparing it to the original number.

    Args:
        x (int): integer value that is being tested for palindromeness using the
            provided algorithm.

    Returns:
        bool: a boolean value indicating whether the given number is a palindrome.

    """
    if x < 0:
        return False
    reversed_x = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        reversed_x = reversed_x * 10 + digit
        temp //= 10
    return x == reversed_x

def roman_to_int(s):
    """
    converts a Roman numeral string to its corresponding integer value using a
    mapping of symbols to values.

    Args:
        s (str): Roman numeral to be converted to its equivalent integer value.

    Returns:
        int: an integer representing the decimal equivalent of a Roman numeral.

    """
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def is_valid(s):
    """
    evaluates a given string for syntax errors, using a stack to track opened
    brackets and ensure proper closing. If no closing bracket is found, the function
    returns False.

    Args:
        s (str): 100 or fewer characters of code to be analyzed for validity.

    Returns:
        int: a boolean indicating whether a given string of characters is valid
        according to a set of rules represented by a mapping of characters to parentheses.

    """
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets_map:
            top_element = stack.pop() if stack else '#'
            if brackets_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

if __name__ == '__main__':
    app.run(debug=True)
