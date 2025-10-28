FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/

# Copy other necessary files
COPY pyproject.toml .
COPY .gitignore .
COPY README.md .

# Command to run the application
CMD ["python", "src/main.py"]