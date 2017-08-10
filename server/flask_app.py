from flask import Flask

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/agent', methods=['GET'])
def get_agent_list():
    return "{'agent_1': '1.2.3.4'}"


@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist", 404

if __name__ == '__main__':
    app.run(debug=True)