# Omamori Finder - Server

## About

Omamori Finder is an application where users can pin their newly discovered omamori on a map, so that other users can go and collect them as well.

## Prerequisites

1. [pip](https://pypi.org/project/pip/)
2. minimum [Python 3.11](https://www.python.org/downloads/)

## Setup

### 1. Setup a virtual enviroment.

```
py -m venv venv
```

### 2. Install dependencies.

```
pip install -r requirements.txt
```

### 3. Setting up the Database

We are currently using a local PostgreSQL database. To get started, please configure your own local database and ensure the correct information is filled in the .env file.

#### 3.a. Setting up AWS S3 bucket

For now create your own S3 bucketand ensure correct information is filled in the .env file.

## 4. Run the API

```
py manage.py runserver
```
