# 1. Base image
FROM python:3.12-slim


# 3. Set work directory
WORKDIR /app

# 4. Install dependencies
COPY requirments.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

# 5. Copy project
COPY . /app/

EXPOSE 8080
# 7. Run entrypoint
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
