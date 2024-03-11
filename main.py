from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    retrieves user input from a JSON object and returns it if available, or `None`
    otherwise.

    Returns:
        float: a JSON serialized list of integers if the request is successful,
        or `None` otherwise.

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes an input list of numbers and returns a list of squared numbers, or `None`
    if no number is provided.

    Args:
        numbers (list): sequence of integers to be squared, and its value is
            examined to determine the output of the `process_input()` function.

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
    takes a list of numbers as input, squares them and returns the result as a
    JSON object with a 200 status code if the input is valid, or a 400 status code
    with an error message otherwise.

    Args:
        squared_numbers (list): number of squared values to display in the output.

    Returns:
        JSON object.: a JSON object containing the squared numbers or an error
        message if no numbers were provided.
        
        		- The first property is `squared_numbers`, which is a list of numbers
        that have been squared.
        		- The second property is `status_code`, which is an integer value
        indicating the HTTP status code of the response. In this case, it is set
        to 200.
        
        	The output returned by the function is a dictionary object with these two
        properties.
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    takes a list of user input numbers, squares each number, and displays the result.

    Returns:
        int: a list of square numbers computed from user-inputted values.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
