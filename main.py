from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_id = {
        "user_id":user_id,
        "name":"Diya Malik",
        "email":"diyamalik@google.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_id["extra"] = extra

    return jsonify(user_id),200

@app.route('/create-user',methods=['POST','PUT'])
def create_user():
    if request.method=='POST':
        data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)


