# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    unzip \
    curl \
    xvfb \
    wget \
        bzip2 \
        snapd

# Chrome
RUN apt-get update && \
  apt-get install -y gnupg wget curl unzip --no-install-recommends && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update -y && \
  apt-get install -y google-chrome-stable && \
  CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
  DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
  wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
  unzip /chromedriver/chromedriver* -d /chromedriver

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to avoid chrome crashes (sandboxing issues)
ENV DISPLAY=:99

# Make the bash script executable (to run tests and send results)
RUN chmod +x /app/notify.sh

# Run the bash script by default when the container starts
CMD ["./run_and_notify.sh"]
