from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <title>Dockerized Flask App</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 80px;">
            <h1>🚀 Welcome to My Dockerized Flask Application!</h1>

            <h2>Siddheshwar Datta Shinde</h2>

            <p>Cloud & DevOps Enthusiast</p>

            <hr width="50%">

            <h3>Tech Stack</h3>
            <p>Python | Flask | Docker | Linux</p>

            <h3>Current Learning Journey</h3>
            <p>
                ✔ Docker<br>
                ✔ AWS<br>
                ✔ Terraform<br>
                ✔ Linux<br>
                ✔ Kubernetes (In Progress)
            </p>

            <hr width="50%">

            <p><strong>Container Status:</strong> Running Successfully ✅</p>
            <p><strong>Application:</strong> Flask Web App</p>

            <h3>Keep Learning. Keep Building. 🚀</h3>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0')