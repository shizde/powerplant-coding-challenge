from flask import Flask, request, jsonify
from methods import calculate_production_plan
app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def productionplan():
    try:
        payload = request.get_json()
        if not payload:
            raise ValueError("Invalid or missing payload")
        return calculate_production_plan(payload), 200

    except Exception as e:
        return {"error": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(debug=True,port=8888)