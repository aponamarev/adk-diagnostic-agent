# Use a minimal Python 3.12 image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install PDM - a modern Python package manager
RUN pip install pdm

# Copy PDM dependency definition files
COPY pdm.lock pyproject.toml ./

# Install project dependencies
RUN pdm install --prod

# Copy the application source code
COPY src/ ./src/
