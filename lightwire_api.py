from flask import Flask, jsonify, make_response
from lightwire_service import get_usage_data

app = Flask(__name__)

@app.route('/')
def index():
    return "Nothing to see here move along"

@app.route('/api/getusagedata')
def get_lightwire_usage_data():
     return jsonify(get_usage_data())

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)    

if __name__ == '__main__':
    app.run(debug=True)