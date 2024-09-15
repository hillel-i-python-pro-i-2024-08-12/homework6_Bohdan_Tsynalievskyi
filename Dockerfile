FROM python:3.12

RUN useradd -ms /bin/bash appuser

WORKDIR /home/appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

RUN chown -R appuser:appuser /home/appuser

USER appuser

ENTRYPOINT ["python", "./main.py"]
