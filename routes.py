from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def get_map():
    return render_template("map.html")

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route('/arrivals', methods=['GET'])
def get_bus_coords():
    API_KEY = "F02CFCAC-3067-45DB-835E-A102C773D6F2"
    stop_ID = request.args.get('stop', 46)  

    url = f"http://api.thebus.org/arrivalsJSON/?key={API_KEY}&stop={stop_ID}"
    
    """
format:

data = {
        "arrivals" : [
            { ...,
              ...,
              ... 
            },

            { ...,
              ...,
              ...
            }
        ],
        "stop_ID" = __,
        "timestamp" = ____
    }
    """
    try:
        response = requests.get(url)

        data = response.json()

        data["arrivals"] = [arrival for arrival in data["arrivals"] 
                    if float(arrival["latitude"]) != 0 and float(arrival["longitude"]) != 0]
                
        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500



if __name__ == '__main__':
    app.run(debug=True)
