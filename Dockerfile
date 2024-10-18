# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask app code into the container
COPY app /app

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variables
ENV FLASK_ENV=development

# Run the Flask app
CMD ["python", "main.py"]
