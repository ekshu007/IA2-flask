from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure your database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ekshu@BtechRvu2023",
    database="ekshu"
)

cursor = db.cursor()

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        query_type = request.form['query_type']
        message = request.form['message']

        # Execute SQL query to insert data into database
        sql = "INSERT INTO contacts (name, email, mobile, query_type, message) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, mobile, query_type, message)
        cursor.execute(sql, values)
        db.commit()

        return "Contact submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)


