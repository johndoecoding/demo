from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_input():
    try:
        numbers = request.json['numbers']
        return numbers
    except KeyError:
        return None

def process_input(numbers):
    if numbers:
        squared_numbers = [num ** 2 for num in numbers]
        return squared_numbers
    else:
        return None

def display_result(squared_numbers):
    if squared_numbers:
        return jsonify({'squared_numbers': squared_numbers}), 200
    else:
        return jsonify({'error': 'No numbers provided.'}), 400

@app.route('/square', methods=['POST'])
def square_numbers():
    numbers = get_user_input()
    squared_numbers = process_input(numbers)
    return display_results(square_numbers)

if __name__ == '__main__':
    app.run(debug=True)
