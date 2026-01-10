# Use the official Python slim image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# set up local package paths
COPY pyproject.toml ./
COPY src/db ./src/db
COPY src/api ./src/api
COPY src/config.py ./src/

RUN pip install .

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY tests ./tests

# Define the command to run the application when the container starts
CMD ["python", "./your_application.py"]