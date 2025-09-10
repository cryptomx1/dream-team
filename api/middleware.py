from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []  # list of dicts: {'from': 'ai_name', 'content': 'text', 'to': 'optional'}

@app.route('/post_message', methods=['POST'])
def post_message():
    data = request.json
    messages.append(data)
    return jsonify({'status': 'success'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    messages.clear()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5000)