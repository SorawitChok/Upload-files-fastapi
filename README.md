# FastAPI File Upload Service
This project is a simple file upload service built using FastAPI, SQLAlchemy, and SQLite. The service allows users to upload files, which are then securely stored on the server with their filenames recorded in a database

## Features
- ***FastAPI***: High-performance, easy-to-use Python web framework.
- ***SQLAlchemy***: ORM for managing database interactions.
- ***SQLite***: Lightweight database for storing file metadata.
- ***File Storage***: Files are saved securely on the server with their original names.

## Setup

### Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

### Installation
1. Clone this repository:

   ```bash
   git clone https://github.com/SorawitChok/fastapi-file-upload.git
   cd fastapi-file-upload
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```
The service will be running at ```http://localhost:5000/```.

## Usage
### File Upload
You can upload files by sending a POST request to the root endpoint (/). The file will be stored in the static/ directory, and its metadata will be saved in the database.
```
import requests

post_url = "http://localhost:5000/"
file_path = "path_to_your_file.txt"

with open(file_path, "rb") as file:
    response = requests.post(post_url, files={"file": file})

print(response.json())
```
### Database Schema
The service uses SQLite to store metadata about the uploaded files. The upload_file table contains the following columns:

- ***id***: Auto-incrementing primary key.
- ***create_date***: Timestamp of when the file was uploaded.
- ***old_name***: Original filename of the uploaded file.
- ***new_name***: Secured filename used for storage.

### Endpoints
- POST /: Upload a file to the server.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.



