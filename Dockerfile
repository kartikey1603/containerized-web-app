FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code in container
COPY . .

EXPOSE 5000

# To run the application
CMD ["python", "app.py"]
