# Lab Journal 2: Docker Compose for Multi-Database Environments

This repository contains the files for Lab Journal 2 of the Introduction to Big Data course at Bahria University, Lahore Campus. This lab focuses on getting hands-on experience with Docker Compose to set up and manage a multi-database environment.

***

## Lab Objective

The main goal is to prepare your system for Docker Compose, configure services for three different databases (Elasticsearch, MongoDB, PostgreSQL), and verify that they are all running and communicating correctly.

***

## Getting Started

### Prerequisites

* **Docker Desktop** (for Windows/macOS) must be installed. For Linux, you need **Docker Engine** and **Docker Compose**.
* Ensure the Docker service is running on your machine.

### Installation

1.  Clone this repository to your local machine.

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  Create a file named **`.env`** in the root directory and add the following:

    ```
    ELASTICSEARCH_PORT=9200
    MONGO_PORT=27017
    POSTGRES_PORT=5432
    POSTGRES_USER="Muhammad Wasiq"
    POSTGRES_PASSWORD=11335577
    POSTGRES_DB=mydatabase
    ```
    **Note**: The username "Muhammad Wasiq" must be in quotes due to the space.

### Running the Services

1.  In your terminal, navigate to the directory where the `docker-compose.yml` file is located.

2.  Run the following command to start all services in the background.

    ```bash
    docker-compose up -d
    ```

***

## Verification

To confirm that your services are working, follow these steps.

### Step 1: Check Container Status

Run this command to see a list of your containers. They should all show a state of **`Up`**.

```bash
docker-compose ps
