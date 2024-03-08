from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    is given a `request` parameter that contains a JSON object with a 'numbers'
    key. The function returns the value of the 'numbers' key if it exists, or None
    otherwise.

    Returns:
        `object`.: a list of integers, or `None` if no user input was provided.
        
        		- The function returns an `None` value when the `request.json` dictionary
        does not contain the key `numbers`.
        		- The `numbers` variable returned by the function is a list of numbers.
        

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes a list of numbers as input and returns a list of squared values of those
    numbers.

    Args:
        numbers (list): 1D list of numbers to be processed by the function, and
            its value is used to calculate and return the squared values of those
            numbers.

    Returns:
        list: a list of squares of the input numbers.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes an input of squared numbers, processes it, and returns the result as a
    JSON object with either a 200 status code or an error message if no numbers
    are provided.

    Args:
        squared_numbers (list): array of integers that should be squared before
            they are displayed as JSON output.

    Returns:
        dict: a JSON response containing an error message if no numbers were
        provided, or the squared values of the given numbers otherwise.

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    takes a list of numbers from user input, processes it by squaring each number
    and returns the result as a list of squared numbers to be displayed to the user.

    Returns:
        int: a list of squared numbers.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
