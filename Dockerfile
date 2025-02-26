FROM python:3.9-slim
RUN apt update && apt install -y zlib1g-dev libpng-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ /app/src

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH="/app/src"

# Command for testing
CMD ["python", "-m", "unittest", "discover", "-s", "src/test", "-p", "test_*.py"]
