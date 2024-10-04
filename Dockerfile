# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster

# Set the working directory inside the container
WORKDIR /app


# Install dependencies
RUN apt-get update && \
    apt-get install -y xvfb gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to avoid chrome crashes (sandboxing issues)
ENV DISPLAY=:99

# Make the bash script executable (to run tests and send results)
RUN chmod +x /app/notify.sh

# Run the bash script by default when the container starts
CMD ["./run_and_notify.sh"]
