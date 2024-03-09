from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    is defined to receive a JSON payload containing a list of numbers, and if
    present, returns that list; otherwise, it returns `None`.

    Returns:
        `object`.: a list of integers represented as JSON.
        
        	The returned value is either an array of numbers or `None`, depending on
        whether a valid JSON object containing numbers was provided in the request
        or not.
        

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes a list of integers as input, performs squaring operation on each element
    in the list and returns the squared list as output.

    Args:
        numbers (list): 1-dimensional array or list of integers to be squared.

    Returns:
        list: a list of squared numbers.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes a list of numbers as input, squares them if they are not empty, and
    returns them as a JSON object with a status code of either 200 (if successful)
    or 400 (if an error occurs).

    Args:
        squared_numbers (int): list of numbers to be squared.

    Returns:
        JSON object.: a JSON object containing the squared numbers if provided,
        and an error message otherwise.
        
        		- The output is a tuple containing two elements: a dictionary with
        key-value pairs representing the squared numbers and an integer status
        code indicating the result (200 for successful execution or 400 for error).
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    processes user input and returns the resulting squared numbers after processing.

    Returns:
        int: a list of square numbers calculated from user input.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
