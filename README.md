# Job Scraper Project

## Overview
This project is a web scraping application built with Scrapy that extracts job listings from JSON files and stores the data in a PostgreSQL database. It also utilizes Redis for caching to avoid duplicate processing of job entries.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Pipeline Process](#pipeline-process)
- [Configuration](#configuration)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sinancansevinc/job-scraper.git
   cd job-scraper
   ```

2. **Install Docker and Docker Compose**
   Ensure you have Docker and Docker Compose installed on your machine. You can download them from the official Docker website.

3. **Create a `.env` File**
   Create a `.env` file in the root directory of the project to store your environment variables. Here’s an example of what to include:
   ```env
   POSTGRES_HOST=postgres
   POSTGRES_DB=jobs_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=canaria+20102024

   REDIS_HOST=redis
   REDIS_PORT=6379
   REDIS_DB=0
   ```

4. **Build the Docker Containers**
   Run the following command to build the Docker containers:
   ```bash
   docker-compose build
   ```

## Running the Project

1. **Start the Services**
   Use Docker Compose to start the services:
   ```bash
   docker-compose up
   ```

   This command will start the Scrapy spider, PostgreSQL database, and Redis service.

2. **Run the Query Script (Optional)**
   After the Scrapy spider has finished running, you can execute the query script to fetch the data from PostgreSQL and save it to a CSV file:
   ```bash
   docker-compose run query
   ```

   This will create a `jobs_data.csv` file in the current directory.

## Pipeline Process

The pipeline process consists of the following steps:

1. **Data Extraction**: The Scrapy spider reads job listings from JSON files (`s01.json`, `s02.json`, etc.) and extracts relevant fields.

2. **Caching with Redis**: Before inserting a job into the PostgreSQL database, the pipeline checks if the job (identified by its `slug`) is already cached in Redis. If it is cached, the job is skipped to avoid duplicates.

3. **Data Insertion**: If the job is not cached, it is inserted into the PostgreSQL database, and the job data is cached in Redis for future reference.

4. **Data Retrieval**: The `query.py` script can be run to retrieve all job entries from the PostgreSQL database and save them to a CSV file.

## Configuration

- **PostgreSQL**: The PostgreSQL database is configured to store job listings. Ensure that the database credentials in the `.env` file match your setup.

- **Redis**: Redis is used for caching job entries. The Redis service is configured in the `docker-compose.yml` file.

- **Scrapy Settings**: The Scrapy settings can be modified in the `settings.py` file located in the `jobs_project/jobs_project` directory.