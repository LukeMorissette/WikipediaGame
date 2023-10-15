from flask import Flask, request, jsonify
import crawler

app = Flask(__name__)

@app.route('/find_path', methods=['POST'])
def find_path():
    data = request.get_json()
    start_page = data['start']
    finish_page = data['finish']

    path = crawler.find_path(start_page, finish_page)

    return jsonify({'path': path})

if __name__ == '__main__':
    app.run(port=5000)
