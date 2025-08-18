# Docker 
Docker is a platform that allows you to **build, package, and run applications** in lightweight, portable containers. 

Docker is a tool that uses OS-level virtualization to deliver software in packages called containers. 

It ensures that your app runs the same way on any system without worrying about dependencies or environment setup.

Containers are isolated environments that include everything needed to run an application, such as code, runtime, libraries, and system tools. This means you can run your application consistently across different environments, whether it's on your local machine, a server, or in the cloud.

Docker simplifies the process of deploying applications by encapsulating them in containers, which can be easily shared and run anywhere Docker is installed. This eliminates the "it works on my machine" problem, as the container includes all dependencies and configurations needed to run the application.

Docker images are the blueprints for containers, containing the application code and its dependencies. You can create your own images using a `Dockerfile`, which is a text file that contains instructions on how to build the image.

Docker File -->  Docker Image -->  Docker Container

# General Docker File Template
```dockerfile
# Use an official base image
FROM base_image:tag
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y package_name
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
# Run app.py when the container launches
CMD ["python", "app.py"]
```

# Example Docker File 
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
# Run app.py when the container launches
CMD ["python", "app.py"]
```

# Command Line Usage
```bash
# Build the Docker image
docker build -t image_name:version .
# Run the Docker container
docker run -p 5000:80 image_name:version
# Stop the running container
docker stop container_id
# Remove the Docker container
docker rm container_id
# Push the Docker image to Docker Hub
docker push image_name:version
# Pull a Docker image from Docker Hub
docker pull image_name:version
# List all Docker images
docker images
# List all running Docker containers
docker ps
# List all Docker containers (including stopped ones)
docker ps -a
# Remove a Docker image
docker rmi image_name:version
# Remove a Docker container
docker rm container_id
# Docker Examples Repository
This repository contains multiple examples of how to use Docker with different technologies such as Python, HTML, and .NET. 
Each folder has its own Dockerfile and source code demonstrating how to containerize different applications.
```

# Docker Examples

This repository contains multiple examples of how to use **Docker** with different technologies such as Python, html, and .NET.  
Each folder has its own `Dockerfile` and source code demonstrating how to containerize different applications.

## 📂 Project Structure
│── python_example1/ # Simple Python app example "Hello World"

│── python_example2/ # Simple Python app example to display image using Flask

│── simple_login_page/ # Simple login page using HTML and CSS

│── simple-dotnet/ # .NET console app example


## ⚙️ Installation

To run these examples, you need **Docker Desktop** installed on your system.  
👉 Follow the official installation guide here:  
[Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

After installation, verify Docker is working by running the following command in your terminal or command prompt:
```bash

docker --version
```
You should see the installed Docker version.

## 🚀 Running the Examples

To run any of the examples, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the example directory you want to run, e.g., `cd python_example1`.
3. Build the Docker image using the following command:
```bash
docker build -t image_name:version .
``` 
4. Run the Docker container using the following command:
```bash
docker run image_name:version

```
   If the application requires a specific port to be exposed, you can use the `-p` flag to map the container's port to your local machine's port. For example, if the application runs on port 5000, you can run:
```bash

docker run -p 5000:5000 image_name:version
```
5. If the application is a web app, open your web browser and go to `http://localhost:5000` to see the application running, else check the console output for any other instructions.   


## 📝 Notes
- Each example has its own `Dockerfile` that defines how to build the Docker image.
- The `docker build` command creates a Docker image from the `Dockerfile`.  
- The `docker run` command starts a container from the built image and maps the container's port to your local machine's port.
- You can stop the running container by pressing `Ctrl+C` in the terminal where you ran the `docker run` command.   
- Docker images can be pushed to Docker Hub or any other container registry for sharing and deployment. 

## 📚 Resources
- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Hub](https://hub.docker.com/) - A repository for Docker images.       
- [Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/) - A quick reference guide for Docker commands.