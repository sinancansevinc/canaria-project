FROM python:3.9


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


WORKDIR /app/jobs_project


ENV PYTHONPATH="/app:${PYTHONPATH}"


CMD ["scrapy", "crawl", "job_spider"]
