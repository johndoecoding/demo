from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    is designed to receive and process user input data from a JSON request. If the
    input data is present, it returns the input data. Otherwise, it returns `None`.

    Returns:
        int: a list of integers representing user input.

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes a list of numbers as input and returns their squared values if they are
    not empty, or `None` otherwise.

    Args:
        numbers (list): 1D list or iterable of non-negative integers that will be
            squared in the function.

    Returns:
        dict: a list of square numbers.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes a list of numbers as input, squared them if present and returns a JSON
    response with the squared numbers or an error message if no numbers are provided.

    Args:
        squared_numbers (list): square of a number, as indicated by its name and
            context in the function.

    Returns:
        dict: a JSON object containing the squared numbers, or an error message
        if no numbers were provided.

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    receives a list of numbers from the user through the `get_user_input()` function,
    squares each number using the `process_input()` function, and returns the
    squared numbers to the user through the `display_result()` function.

    Returns:
        float: a list of numbers squared.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
