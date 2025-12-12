# monitoring/Dockerfile

FROM python:3.10-slim

WORKDIR /monitoring

COPY . .

RUN pip install jupyter pandas matplotlib

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
