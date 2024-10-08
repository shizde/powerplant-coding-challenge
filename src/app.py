from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def productionplan():
    payload = jsonify(request.json)
    return payload

if __name__ == '__main__':
    app.run(debug=True,port=8888)