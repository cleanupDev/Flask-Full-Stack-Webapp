from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'status': 'success',
                    'message': 'Hello World'
                    }), 200


@app.route('/<name>')
def hello_name(name):
    return jsonify({'status': 'success',
                    'message': 'Hello {}'.format(name)
                    }), 200


if __name__ == '__main__':
    app.run(debug=True)
