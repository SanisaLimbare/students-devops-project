
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Information System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 850px;
                margin: 40px auto;
                padding: 20px;
                background-color: #f3f6fb;
                color: #263238;
                line-height: 1.6;
            }
            h1 {
                color: #174ea6;
                text-align: center;
            }
            .subtitle {
                text-align: center;
                color: #546e7a;
            }
            .card {
                background: white;
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
                box-shadow: 0 2px 8px #00000012;
            }
            h2 {
                color: #174ea6;
            }
            .status {
                color: #16803c;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Student Information System</h1>
        <p class="subtitle">End-to-End DevOps Mini Project</p>

        <div class="card">
            <h2>About the Project</h2>
            <p>This project demonstrates the development and deployment
            of a web application using modern DevOps practices. It
            automates software testing, containerization, and deployment
            through a Continuous Integration and Continuous Deployment
            (CI/CD) pipeline.</p>
        </div>

        <div class="card">
            <h2>Technologies Used</h2>
            <ul>
                <li><b>Python and Flask:</b> Web application development</li>
                <li><b>Pytest:</b> Automated application testing</li>
                <li><b>Git and GitHub:</b> Version control and source code management</li>
                <li><b>Jenkins:</b> CI/CD pipeline automation</li>
                <li><b>Docker:</b> Application containerization and deployment</li>
            </ul>
        </div>

        <div class="card">
            <h2>CI/CD Pipeline</h2>
            <p>Source Code → GitHub → Jenkins → Automated Tests
            → Docker Image → Container Deployment</p>
            <p class="status">Application deployed successfully!</p>
        </div>

        <div class="card">
            <h2>Application Health</h2>
            <p>Check whether the application is running correctly:</p>
            <a href="/health">View Health Status</a>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
