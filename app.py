from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return f"""
    <h1>🚀 DevOps Projects Dashboard - Green</h1>

    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Last Updated:</b> {datetime.utcnow()}</p>

    <hr>

    <ul>
        <li><a href="/project1">Project 1: Linux + Git + Docker</a></li>
        <li><a href="/project2">Project 2: GitHub Actions + EC2</a></li>
        <li><a href="/project3">Project 3: Docker Hub CI/CD</a></li>
        <li><a href="/project4">Project 4: AWS ECS + Fargate</a></li>
    </ul>
    """

# Project 1 Page
@app.route("/project1")
def project1():
    return """
    <h2>Project 1</h2>
    <p>Static application containerized using Docker and deployed on EC2.</p>
    <a href="/">⬅ Back</a>
    """

# Project 2 Page
@app.route("/project2")
def project2():
    return """
    <h2>Project 2</h2>
    <p>CI/CD pipeline using GitHub Actions to deploy containers to EC2.</p>
    <a href="/">⬅ Back</a>
    """

# Project 3 Page
@app.route("/project3")
def project3():
    return """
    <h2>Project 3</h2>
    <p>Docker image build and push to Docker Hub with automated deployment.</p>
    <a href="/">⬅ Back</a>
    """

# Project 4 Page
@app.route("/project4")
def project4():
    return """
    <h2>Project 4</h2>
    <p>Python Flask app deployed to AWS ECS Fargate using GitHub Actions.</p>
    <a href="/">⬅ Back</a>
    """

# App Runner (ONLY ONE)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
