from flask import Flask, jsonify, Response
import logging

app = Flask(__name__)

@app.route('/')

def api_root():
    data = {
        'service_name'  : 'python3-example',
        'user' : 'foo'
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

    logging.info('status OK')
    
@app.route('/health')

def api_health():
    data = {
        'status' : 'health'
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

    logging.info('status OK')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')