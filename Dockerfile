# Use a lightweight, secure Python runtime based on Alpine Linux
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required to build certain Python extensions
RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev

# Copy the dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the internal port the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
