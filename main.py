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

if __name__ == '__main__':
    app.run(debug=True)
