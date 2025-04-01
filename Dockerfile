# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to disable Streamlit warnings
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=False

# Expose Streamlit's default port (8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
