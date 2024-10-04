FROM selenium/standalone-chrome:latest

WORKDIR /app
COPY . /app

# RUN apt-get update && apt-get install -y curl && apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

# ENV DISCORD_WEBHOOK_URL=""



# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    xvfb \
    gnupg2 \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libgbm-dev \
    libx11-xcb1 \
    libxcomposite1 \
    libxrandr2 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') \
    && CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") \
    && wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P /tmp \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to avoid chrome crashes (sandboxing issues)
ENV CHROME_BIN="/usr/bin/google-chrome"
ENV DISPLAY=:99

# Make the bash script executable (to run tests and send results)
COPY run_and_notify.sh /app/run_and_notify.sh
RUN chmod +x /app/notify.sh

# Run the bash script by default when the container starts
CMD ["./run_and_notify.sh"]
