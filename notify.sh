#!/bin/bash

if [ -z "$DISCORD_WEBHOOK_URL" ]; then
    echo "Error: DISCORD_WEBHOOK_URL environment variable is not set."
    exit 1
fi

python main.py

LOG_FILE="test_log.log"
if [ -f "$LOG_FILE" ]; then
    echo "Log file $LOG_FILE created."

    ERRORS_COUNT=$(grep -c "FAILED" "$LOG_FILE")
    PASSED_COUNT=$(grep -c "PASSED" "$LOG_FILE")
    TESTS_COUNT= $((ERRORS_COUNT + PASSED_COUNT))

    CURRENT_DATE=$(TZ=Etc/GMT-2 date +"%Y-%m-%d %H:%M:%S")
    ROLE_ID="1174437656688607353"
    MSG="<@&$ROLE_ID>\n## Frontend Tests performed on __ $CURRENT_DATE __ ($INFO_LABEL)"
    SUMMARY="Tests completed: $TESTS_COUNT\nPassed: **$PASSED_COUNT**\nErrors: **$ERRORS_COUNT**"

    curl -H "Content-Type: application/json" \
      -X POST \
      -d '{
        "content": "'"${MSG}"'",
        "embeds": [{
          "title": "Frontend Test Summary",
          "description": "'"${SUMMARY}"'",
          "color": 15924992
        }]
      }' \
      "$DISCORD_WEBHOOK_URL"

    echo "Summary sent to Discord webhook."

    curl -X POST \
      -H "Content-Type: multipart/form-data" \
      -F "file=@$LOG_FILE" \
      "$DISCORD_WEBHOOK_URL"

    echo "Log file sent to Discord webhook."
else
    echo "Log file $LOG_FILE not found. Exiting."
fi
