FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install pandas spacy matplotlib seaborn

# Download the English model for spaCy
RUN python -m spacy download en_core_web_sm

# Run paragraphs.py when the container launches
CMD ["python", "paragraphs.py"]






