FROM python:3.12

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /home/appuser

COPY requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

COPY main.py .

RUN chown --recursive appuser:appuser /home/appuser

USER appuser

ENTRYPOINT ["python", "./main.py"]
