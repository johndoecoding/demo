from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    retrieves a list of numbers from an input provided by a previous request.

    Returns:
        `Optional[number]`.: a list of integers represented as JSON data.
        
        	The returned value is of type `numbers`, which suggests that it is a list
        or array of numerical values.
        

    """
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    """
    takes an input list of numbers and returns a list of squares of those numbers.
    If no number is provided, it returns `None`.

    Args:
        numbers (`iterable`.): 1-dimensional array of integers to be processed and
            returned as squared values.
            
            		- ` numbers` is a list of values that are to be squared.
            		- The values in the list can be any number type, including integers,
            floats, or complex numbers.
            		- Each value in the list is squared using the element-wise multiplication
            operation `**`.
            

    Returns:
        float: a list of square numbers generated from the input arguments.

    """
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    """
    takes an iterable `squared_numbers` as input and returns a JSON response with
    an error message if no numbers are provided or a success message with the
    squared numbers otherwise.

    Args:
        squared_numbers (list): array of numbers that will be squared and returned
            as a JSON response in the function `display_result`.

    Returns:
        JSON object.: a JSON object containing the squared numbers if provided,
        and an error message if not.
        
        		- The first property is `'squared_numbers'`, which contains the list of
        squared numbers provided in the input argument.
        		- The second property is the HTTP status code, which is set to 200 in
        case the input list is not empty, and 400 otherwise.
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    takes a list of numbers as input, processes them using a calculation, and
    displays the resulting squared values to the user.

    Returns:
        list: a list of squared numbers computed from user input.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
