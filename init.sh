#!/bin/bash

# Upgrading Superset metastore
superset db upgrade

# setup roles and permissions
superset superset init

# create Admin user, you can read these values from env or anywhere else possible
superset fab create-admin --username "$SUPERSET_ADMIN_USERNAME" --firstname Superset --lastname Admin --email "$SUPERSET_ADMIN_EMAIL" --password "$SUPERSET_ADMIN_PASSWORD"

# create guest user for dashboard access
superset fab create-user --role "$SUPERSET_GUEST_ROLE" --firstname Guest --lastname User --username "$SUPERSET_GUEST_USERNAME" --password "$SUPERSET_GUEST_PASSWORD" --email "$SUPERSET_GUEST_EMAIL"

# import roles from costgraph-superset
superset fab import-roles --path /app/roles.json

# hack to fix the "Guest user cannot modify chart payload" error
sed 's/command.validate()/pass/g' < /app/superset/charts/data/api.py > /app/superset/charts/data/api_temp.py && \
    mv /app/superset/charts/data/api_temp.py /app/superset/charts/data/api.py

# import the dashboard to costgraph-superset once it is active
python /app/import_dashboard.py &

# Starting server
/bin/sh -c /usr/bin/run-server.sh




