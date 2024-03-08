from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    retrieves user input from a JSON payload and returns it as a number value.

    Returns:
        None: a list of integers, or `None` if no input was provided.

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes a list of numbers as input, squares each number in the list, and returns
    the squared numbers.

    Args:
        numbers (list): 0 or more input values that are processed by the function.

    Returns:
        list: a list of square numbers.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes an input list of numbers and squares each number, returning a JSON
    response with either the squared numbers or an error message if no numbers
    were provided.

    Args:
        squared_numbers (int): list of numbers to be squared for output as JSON data.

    Returns:
        `json` object.: a JSON response containing either the squared numbers or
        an error message if no numbers were provided.
        
        		- `squared_numbers`: This is a list of numbers that were provided to the
        function.
        		- `status_code`: This is an integer representing the HTTP status code
        of the response. In this case, it is 200, indicating a successful response.
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    processes user input, squares each number, and displays the squared result.

    Returns:
        int: the list of numbers squared.

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
