# Step: Install official Python base image
FROM python:3.8

# Step: Set working directory inside the container
WORKDIR /myapp

# Step: Install appropriate dependencies
RUN apt-get -y update  && apt-get install -y \
    python3-dev \
    apt-utils \
    python-dev \
    build-essential \   
&& rm -rf /var/lib/apt/lists/* 

# Step: Copy everything to workdir inside container
COPY . .

# Step: Install required python dependencies from requirements file
RUN pip install --no-cache-dir -U -r requirements.txt


# Step: Expose the port Flask is running on
EXPOSE 8000

# Step: Run Flask
CMD uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000