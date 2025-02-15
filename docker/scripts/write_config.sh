#!/bin/bash

echo "telegram_token=${TG_TOKEN}" > /data/send-to-archivebox/src/config.py
echo "whitelist={${WHITELIST}}" >> /data/send-to-archivebox/src/config.py
echo "archivebox_username=${ARCHIVEBOX_USER}" >> /data/send-to-archivebox/src/config.py
echo "archivebox_password=${ARCHIVEBOX_PASS}" >> /data/send-to-archivebox/src/config.py
echo "archivebox_url=${ARCHIVEBOX_URL}" >> /data/send-to-archivebox/src/config.py