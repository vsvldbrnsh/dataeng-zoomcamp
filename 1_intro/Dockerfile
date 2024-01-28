FROM python:3.9

RUN pip install pandas pgcli jupyter sqlalchemy psycopg2

WORKDIR /app

COPY jupyter-data/data_ingestion.py data_ingestion.py

# Expose the port Jupyter will run on
EXPOSE 8888

# ENTRYPOINT [ "python", "pipeline.py" ]
ENTRYPOINT [ "python", "data_ingestion.py" ]

# Start Jupyter Notebook server
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--notebook-dir=/app/"]