FROM python:3.9

RUN pip install pandas pgcli jupyter sqlalchemy psycopg2

WORKDIR /app

# Expose the port Jupyter will run on
EXPOSE 8888

# Start Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--notebook-dir=/app/"]