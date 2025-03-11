# Use a Python base image (matching Django's requirements)
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Upgrade pip and install the project dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# # Run database migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# # Collect static files
# RUN python manage.py collectstatic --noinput

# Expose the port that Django will run on (adjust if needed)
EXPOSE 8000

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "MySchool.wsgi:application", "--bind", "0.0.0.0:8000"]