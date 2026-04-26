# DevOps Containerized To-Do Application

A lightweight, containerized task management application built with Python and Flask. This project demonstrates foundational DevOps practices using Docker and Docker Compose.

## 🚀 Features
* Dynamic task addition and deletion.
* Fully isolated Python 3.10 runtime environment.
* Containerized networking exposed on local port 5000.

## 🛠️ Prerequisites
Ensure you have the following installed on your local machine:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Git

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/noeljais/python-todo-docker.git](https://github.com/noeljais/python-todo-docker.git)
   cd python-todo-docker
Build and launch the container:

Bash
docker compose up --build
Access the application:
Open your web browser and navigate to http://localhost:5000.

📁 Project Structure
app.py: The core Flask routing and application logic.

Dockerfile: The blueprint for the Python 3.10 slim container image.

docker-compose.yml: The configuration to map ports and manage the container service.

requirements.txt: The required Python dependencies (Flask).

🔒 Future Enhancements
Deploy the containerized application to cloud infrastructure (AWS EC2 or Azure VNet).

Implement container vulnerability scanning using tools like Trivy.

Perform routine service detection and security hardening against the server environment.
