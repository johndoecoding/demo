from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    """
    retrieves user input as a JSON object and returns its contents if successful,
    or `None` otherwise.

    Returns:
        `object`.: a list of integers.
        
        		- If the `numbers` parameter is provided, it contains a list of numerical
        values.
        		- The list may contain zero or more elements.
        		- Each element in the list is a single numerical value.
        		- The type of each element is an integer or float (dependent on the
        Python version).
        

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
        numbers (`iterable` of `number`s.): 1-dimensional list or sequence of
            non-negative integers to be squared.
            
            		- ` numbers`: It is an instance of `list`, which means it is a
            collection of items that can be of any data type.
            		- `num`: It is the variable name given to each item in the list.
            		- `[num ** 2 for num in numbers]`: This line creates a new list
            called `squared_numbers` containing the squares of each number in the
            original list.
            

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
    takes an iterable of numbers as input, squaring each number, and returning a
    JSON response with either the squared numbers or an error message if no numbers
    are provided.

    Args:
        squared_numbers (list): square of the input number passed to the function,
            which is then returned as an output in the format of a JSON response.

    Returns:
        JSON object.: a JSON response containing either the squared numbers or an
        error message if no numbers were provided.
        
        		- The output is a dictionary containing the key-value pair 'squared_numbers'
        with the value being a list of numbers.
        		- If the `squared_numbers` variable is present in the input argument,
        the output will be a 200 status code response with the dictionary containing
        the squared numbers.
        		- If the `squared_numbers` variable is not present in the input argument,
        the output will be a 400 status code response with an error message
        indicating that no numbers were provided.
        

    """
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    """
    processes user-inputted numbers and returns their squared values after processing
    them.

    Returns:
        float: a list of numbers that have been squared.

    """
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_result(squared_numbers)

if __name__ == '__main__':
    app.run(debug=True)
