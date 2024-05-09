from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ekshu@BtechRvu2023@localhost/ekshu'
# Replace 'username', 'password', and 'db_name' with your actual database credentials and name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    query_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        query_type = request.form['query_type']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, mobile=mobile, query_type=query_type, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return "Contact submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
