FROM python:3.13-slim

# Set working directory
WORKDIR /app

ENV PYTHONPATH="/app"

# Copy requirements from root context (build context = hackathon/)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# ✅ Correct: Copy all of `src/` so the folder structure is preserved
COPY src /app

# Default command
CMD ["python", "LanGraphAgentic/main.py"]