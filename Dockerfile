FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y curl && apt-get clean
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /app/notify.sh

# ENV DISCORD_WEBHOOK_URL=""

CMD ["/app/notify.sh"]
