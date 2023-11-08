# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR ./app

# Copy the local code to the container
COPY ./app /./app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn pydantic statsmodels

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "api_setup:app", "--host", "0.0.0.0", "--port", "8000"]