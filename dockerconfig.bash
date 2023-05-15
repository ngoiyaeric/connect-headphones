#!/bin/bash

# Build the Docker image
docker build -t headphones-connector .

# Run the Docker container with the shared volume
docker run -v /path/to/shared_dir:/app/shared_dir headphones-connector
