from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/arrivals', methods=['GET'])
def get_bus_coords():
    API_KEY = "F02CFCAC-3067-45DB-835E-A102C773D6F2"
    stop_ID = request.args.get('stop', 2)  

    url = f"http://api.thebus.org/arrivals/?key={API_KEY}&stop={stop_ID}"

    try:
        response = requests.get(url)

        data = response.json()

        print(jsonify(data))
        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Ensure this is correctly placed outside the function
if __name__ == '__main__':
    app.run(debug=True)
