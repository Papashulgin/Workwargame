from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/state', methods=['GET'])
def get_state():
    with open('game_state.json') as f:
        state = json.load(f)
    return jsonify(state)

@app.route('/api/state', methods=['POST'])
def update_state():
    data = request.json
    with open('game_state.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "updated"})

if __name__ == '__main__':
    app.run(debug=True)
