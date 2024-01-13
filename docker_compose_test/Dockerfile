# Dockerfile
FROM python:3.8

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Use Gunicorn as the server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
