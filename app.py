@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if len(password) < 6:
        return "Password must be at least 6 characters!"

    with open('users.txt', 'a') as file:
        file.write(f"{name}, {email}, {password}\n")

    return f"User {name} registered successfully!"