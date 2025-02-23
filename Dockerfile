FROM apache/superset:latest

USER root

RUN pip install psycopg2-binary flask-cors requests Flask-Session[cachelib] Flask-Caching

COPY init.sh config.py roles.json import_dashboard.py dashboard.zip  /app/
ENV SUPERSET_CONFIG_PATH /app/config.py

RUN chmod +x /app/init.sh

ENTRYPOINT [ "/app/init.sh" ]