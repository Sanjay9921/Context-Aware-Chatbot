# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Download spaCy language model
RUN python -m spacy download en_core_web_sm

# Copy project files
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py", "--host=0.0.0.0"]