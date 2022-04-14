from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# curl -X POST -H "Content-Type: application/json" -d '{"number": 5}' localhost:8080/getSquare
@app.route('/getSquare', methods=['POST'])
def get_square():
    if not request.json or 'number' not in request.json:
        abort(400)
    num = request.json['number']

    return jsonify({'answer': num ** 2})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
