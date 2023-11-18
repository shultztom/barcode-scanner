FROM python:3.12-bullseye

# Create app directory
WORKDIR /app

# For pyzbar
RUN apt update && apt-get -y install libzbar0

# For opencv
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
