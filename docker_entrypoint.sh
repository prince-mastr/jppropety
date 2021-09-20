#!/bin/sh
cd /opt/codemastr/tagifiles && touch /var/log/nginx/access.log \
&& nginx \
&& gunicorn -k eventlet --log-level ERROR --error-logfile /var/log/gunicorn.log tf_connector.config.wsgi -b 127.0.0.1:4500
