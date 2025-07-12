from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="API aktif!")

@app.route('/sukses')
def sukses():
    return jsonify(message="Hit berhasil!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
