#  Containerized Web Application & Database Environment

##  Project Overview
This project demonstrates the architectural shift from monolithic design to decoupled microservices. It utilizes Docker to containerize a custom Python web application and connects it seamlessly to a relational MySQL database. 

By leveraging Docker Compose, both the application runtime and the database engine are orchestrated simultaneously, communicating securely over an isolated, private Docker network while maintaining persistent data storage.

##  Tech Stack
* **Containerization:** Docker
* **Orchestration:** Docker Compose
* **Backend Runtime:** Python 3.9 (Alpine Linux)
* **Web Framework:** Flask
* **Database:** MySQL 8.0

##  Prerequisites
To run this multi-container environment locally, you only need one tool installed:
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) 
2. [Python 3.x & pip](https://www.python.org/downloads/) 

##  Repository Structure
```text
containerized-web-app/
├── docker-compose.yml     # Orchestration file mapping networks, volumes, and environments
├── Dockerfile             # Blueprint to build the lightweight Python web image
├── app.py                 # The core Flask application with database retry-logic
├── requirements.txt       # Application dependencies (Flask, MySQL connector)
└── .gitignore             # Prevents database storage volumes from entering version control
```

##  Step-by-Step Execution
Step 1: Start the Multi-Container Environment
Open your terminal in the project directory. Run the following command to build the custom application image, pull the MySQL database image, and start both containers in the background:
```bash
docker compose up -d
```

Step 2: Monitor the Database Initialization
Relational databases require a few seconds to configure their schemas upon their very first boot. To watch the containers start up and verify the database is ready, check the logs:

```bash
docker compose logs -f
```
(Note: Press Ctrl + C to exit the log view once the database is ready for connections).

##  Expected Output
To verify that the application container is successfully reading and writing to the database container, open your web browser and navigate to:
http://localhost:8080

You should receive a JSON response similar to this:
 ```bash
JSON
{
  "architecture": "Multi-Container Decoupled Architecture",
  "message": "Connected to the MySQL database successfully over the Docker network!",
  "status": "success",
  "total_database_writes": 1
}
```
Data Persistence Test: Refresh the page multiple times. You will see the "total_database_writes" counter increase. This proves the application is actively writing to the MySQL database.
