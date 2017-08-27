from flask import Flask
import json

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/agent', methods=['GET'])
def get_agent_list():
    data = {"agents": {"1.2.3.4": "socket_object_1", "8.7.6.5": "socket_object_2"}}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.errorhandler(404)
def page_not_found():
    return "This page does not exist", 404

if __name__ == '__main__':
    app.run(debug=True)