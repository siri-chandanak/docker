# Base image
FROM python:3.10-slim

# Copy requirements first (for caching layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .


# Run the app
CMD ["python", "app.py"]
