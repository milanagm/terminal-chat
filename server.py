from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # get the text 
    data = request.get_json()
    
    # Check: is text in json format?
    if not data or "chat" not in data:
        return jsonify({"error": "Invalid input."}), 400

    # Extract the text message
    user_message = data["chat"]
    
    # split message into "Command" und "Message"
    if user_message.startswith("/"):  
        space_index = user_message.find(" ")
        if space_index == -1:
            # No space found, entire string after "/" is the command
            command = user_message[1:]
            message = ""
        else:
            # Split into command and message
            command = user_message[1:space_index]
            message = user_message[space_index + 1:]

    else:  # message doesn't start with "/"
        command = "None"
        message = user_message

    # Formatting
    response = {"chat": f"{command}: {message}"}
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
