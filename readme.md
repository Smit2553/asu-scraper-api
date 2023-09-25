# ASU Course Scraper API

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Running](#running)

## Overview

The ASU Course Scraper API is a tool designed to scrape course information from Arizona State University (ASU) and provide it in a structured format for easy access and integration into various applications.

## Features

- Retrieve course information including course numbers, titles, descriptions, instructors, schedules, and more.
- Search for courses based on criteria such as department, course number, term, and campus.
- Access real-time data directly from ASU's course catalog.
- Easy-to-use API endpoints for seamless integration into your applications.

## Usage

To use the ASU Course Scraper API, follow these steps:

1. **Authentication**: If you are running this locally you do not need an API. A hosted version does not exist yet as this is WIP, it must be self-hosted for now. 
2. **Endpoints**:

   - `/schedule`: Required parameters are subject, course_number and term
   - The format for term is `2YYX` where YY is the last 2 of the current year and X is the semester number (1 for spring, 4 for summer, 7 for fall)

## Running

1. Clone the repository
```bash
git clone https://github.com/Smit2553/asu-scraper-api.git
```
2. Install dependencies
```bash
conda install --file requirements.txt
```
3. Run the server
```bash
uvicorn main:app 
```
**Do not use --reload as an argument for uvicorn since it causes playright to throw an unimplimented error**