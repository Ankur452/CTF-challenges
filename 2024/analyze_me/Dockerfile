# Use a lightweight base image with GCC or Alpine
FROM ubuntu:20.04 

# Install necessary packages (if any)
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the compiled C executable into the container
COPY analyze_me /app/analyze_me

# Expose the port that the server will run on
EXPOSE 2024

# Run the C executable when the container starts
CMD ["./analyze_me"]
