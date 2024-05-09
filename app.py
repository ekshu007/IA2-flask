from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES = [{
    "id": 1,
    "title": "Chip level servicing",
    "description": "Chip level servicing"
}, {
    "id": 2,
    "title": "Networking and Configuring",
    "description": "Network configuration"
}, {
    "id": 3,
    "title": "Closed Circuit Television Systems",
    "description": "Closed circuit TV systems"
}, {
    "id": 4,
    "title": "Firewall",
    "description": "Firewall"
}, {
    "id": 5,
    "title": "Solar panels",
    "description": "sum dolor sit amet, consectetur adipiscing elit."
}]


@app.route("/")
def hello_world():
    return render_template('home.html',
                           services=SERVICES,
                           company_name="Harshitha Technologies")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(SERVICES)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
