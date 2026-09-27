# 1. Base image with lightweight Python 3.11
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

# 4. Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Command to execute the data pipeline when container starts
CMD ["python", "pipeline.py"]