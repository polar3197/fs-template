# Use the official Python slim image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# set up local package paths
COPY pyproject.toml ./
COPY src/db ./src/db
COPY src/api ./src/api
COPY src/config.py ./src/

RUN pip install .

# Copy the requirements file into the container
COPY src/api/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY tests ./tests

# Set PYTHONPATH to include the api directory
ENV PYTHONPATH=/app/src/api

EXPOSE 8000

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
