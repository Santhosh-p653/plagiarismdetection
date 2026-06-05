FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m pip install spacy && \
    python -m spacy download en_core_web_md

COPY . .

EXPOSE 7860

CMD ["python", "app.py"]
