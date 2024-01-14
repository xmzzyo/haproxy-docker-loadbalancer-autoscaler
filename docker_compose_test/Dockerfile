# Dockerfile
FROM python:3.8-alpine

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Use Gunicorn as the server
CMD ["python", "-w", "4", "-b", "0.0.0.0:5678", "app:app"]
