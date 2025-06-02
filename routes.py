from flask import json ,request ,Flask

app=Flask(__name__)

@app.route('/')
def api_root():
    return 'Welocome!'

@app.route('/github', methods=['POST'])
def api_github_msg():
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if data:
            print(data)
            return json.dumps({'status': 'success', 'message': 'Data received successfully!'}), 200
        else:
            return json.dumps({'status': 'error', 'message': 'No data received!'}), 400
        
if __name__ == '__main__':
    app.run(debug=True)