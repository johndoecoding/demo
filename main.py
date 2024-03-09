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

if __name__ == '__main__':
    app.run(debug=True)
