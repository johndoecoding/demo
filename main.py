from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    is given a JSON payload with an element called 'numbers'. It then attempts to
    retrieve those input numbers. If there are no numbers present in the payload,
    it returns `None`.

    Returns:
        float: a JSON-formatted list of numbers if the request includes a `numbers`
        field in the JSON body, and `None` otherwise.

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes an iterable as input and returns a list of squares of the numbers in the
    input.

    Args:
        numbers (`iterable`.): 1-dimensional sequence of non-negative integers to
            be squared, and it is used to determine the result of the `process_input`
            function.
            
            		- If `numbers` is provided, it contains a list of integers.
            		- Each integer in the list has an attribute called `__len__`, which
            returns an integer representing the length of the list.
            		- Each integer in the list also has an attribute called `__iter__`,
            which returns an iterator over the list.
            		- The list `numbers` may be empty (`None`).
            

    Returns:
        `array`.: a list of squares of the input numbers.
        
        		- If the input is not empty (`numbers` is not None), the function returns
        a list of squared numbers, where each number in the input list is raised
        to the power of 2.
        		- Otherwise (`numbers` is None), the function returns `None`.
        

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes a list of integers as input and returns a JSON response with the squared
    values or an error message if no numbers are provided.

    Args:
        squared_numbers (int): list or tuple of integers that will be squared by
            the function and returned as JSON in a response object if present, or
            an error message if empty or nonexistent.

    Returns:
        dict: a JSON object containing either the squared numbers or an error message.

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    receives input numbers from the user, squares them, and returns the squared
    numbers as output.

    Returns:
        int: the squared numbers of the user-provided input.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
