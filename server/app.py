from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Helper function to validate file from base64 string
def validate_file(file_b64):
    try:
        # Check if the file_b64 is a valid base64 string
        base64.b64decode(file_b64)
        # Here you can add additional validation checks for MIME types, file size, etc.
        return True, "application/octet-stream", len(file_b64) / 1024  # Assume a general MIME type for simplicity
    except Exception:
        return False, None, 0

# POST method for processing the input
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.get_json()
    
    # Extract user input (data array and file_b64 if present)
    input_data = data.get('data', [])
    file_b64 = data.get('file_b64', None)

    # Separate numbers and alphabets from the data
    numbers = [item for item in input_data if item.isdigit()]
    alphabets = [item for item in input_data if item.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase = max(lowercase_alphabets, default=None)

    # File validation
    file_valid = False
    file_mime_type = None
    file_size_kb = 0

    if file_b64:
        file_valid, file_mime_type, file_size_kb = validate_file(file_b64)

    # Prepare response
    response = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",  # Replace with your own user_id format
        "email": "your_email@example.com",  # Replace with actual email
        "roll_number": "your_roll_number",  # Replace with your roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response), 200

# GET method for returning the operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
