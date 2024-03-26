## Beginning with API

Flask - is a micro web framework for Python. It is used in web development and API creation.

0. Create virtual environment : `python3 -m venv env`
1. Activate the virtual environment:  
   Windows- `env\Scripts\activate`
   Linux/MacOS - `source env/bin/activate`.

2. Install Flask - `pip3 install flask`

3. Basic Initialization

````from flask import Flask, request, jsonify
app = Flask(__name__)
if __name__ == '__main__': app.run()```

main is the entry point of our application

4. Define the decorator and the function of the API request

a. Prints 'Hello World' on making the api request on the browser locally.

    ```@app.route('/')
        def home():
            return "Hello World"```

b. Creates GET request
Takes the user_id from the url (Path Parameter) and the extra_info (Query Parameter)

    ``` @app.route('/get-user/<user_id>?extra="<extra_info>"')
        def get_user(user_id):
            user_id = {
                "user_id":user_id,
                "name":"Diya Malik",
                "email":"diyamalik@google.com"
            }

            extra = request.args.get("extra")
            if extra:
                user_id["extra"] = extra

            return jsonify(user_id),200```

c. Creates POST request
Takes the user data information from the request body and the functions returns the response with the data
` @app.route('/create-user',methods=['POST','PUT'])
        def create_user():
            if request.method=='POST':
                data = request.get_json()
            return jsonify(data), 201`

6. Run the python application - `python main.py`
   and enter the URL according to the request required mentioned in the decorators.
````
