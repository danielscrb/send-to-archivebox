#!/bin/bash

CONFIG_FILE="/data/send-to-archivebox/src/config.py"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Generating config file"
  cat <<EOF > "$CONFIG_FILE"
telegram_token='${TG_TOKEN}'
whitelist={${WHITELIST}}
archivebox_username='${ARCHIVEBOX_USER}'
archivebox_password='${ARCHIVEBOX_PASS}'
archivebox_url='${ARCHIVEBOX_URL}'
EOF
else
  echo "Config file already exists, skipping generation."
fi

exec "$@"