from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    with open('users.txt', 'a') as file:
        file.write(f"{name}, {email}, {password}\n")

    return f"User {name} registered successfully!"

if __name__ == '__main__':
    app.run(debug=True)