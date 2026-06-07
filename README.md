# Automated Outreach Pipeline

## Overview

This project is a fully automated cold outreach pipeline built using Python.

The system takes a single company domain as input and automatically performs the following stages:

1. Find similar companies
2. Find decision makers
3. Resolve work emails
4. Send personalized outreach emails

The entire pipeline works automatically without manual intervention.

---

## Features

- Fully automated workflow
- Modular architecture
- Email automation using Brevo API
- Safety checkpoint before sending emails
- Clean command-line interface
- Duplicate email prevention

---

## Technologies Used

- Python
- Requests
- Rich
- Python Dotenv
- Brevo API

---

## Project Structure

automated-outreach/
│
├── main.py
├── .env
├── requirements.txt
│
├── services/
│ ├── ocean_service.py
│ ├── prospeo_service.py
│ ├── eazyreach_service.py
│ └── brevo_service.py

---

## Workflow

Input Domain
↓
Find Similar Companies
↓
Find Decision Makers
↓
Resolve Emails
↓
Safety Checkpoint
↓
Send Emails

---

## Setup Instructions

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Add API keys in .env

4. Run the project

python main.py

---

## Future Improvements

- Real Ocean.io integration
- Real Prospeo integration
- Real Eazyreach integration
- CSV export support
- Async processing
- Better personalization engine

---

## Demo Screenshots

### Pipeline Execution

<img width="897" height="470" alt="image" src="https://github.com/user-attachments/assets/a5a05bbd-4b1c-4bd2-8611-4331348c4e98" />


### Email Received

<img width="799" height="278" alt="image" src="https://github.com/user-attachments/assets/19123a10-89cb-4a7d-83fa-62b56b43f430" />



## Author

Sanjana Singh
