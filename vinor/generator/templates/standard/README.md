# Standard

Opensource Portfolio application for python developers based on Python 3 & FastAPI framework.

**Features**

- [x] CRUD Categories
- [x] CRUD Posts
- [x] CRUD Subscriptions
- [ ] Send SMTP Mail
  - [ ] Send mail after subscribe, change password, One-time password (OTP), ..etc 
- [ ] Download CV/Resume

## Quickstart

**Pre-requisites:**

- Python 3.8 & Virtualenv
- SQLAlchemy ORM 
- FastAPI framework.
- SQLite database.

#### Step 1: Create virtualenv with python 3.8+

Move to standard directory:

```shell
cd standard
```

Create virtualenv

```shell
virtualenv -p python3.8 venv3.8
```

Active environment

```shell
source venv3.8/bin/activate
```

#### Step 2: Install Python package dependencies

```shell
pip install -r requirements.txt
```

#### Step 3: Start application

Start application in development mode with live reload

```shell
# Move to project root directory
cd standard

# Run application
uvicorn standard.main:app --reload
```

#### Step 4: Verify application 

Open your browser this address: http://127.0.0.1:8000

```json
{"message":"Welcome to Standard!"}
```

## Testing

This project use Pytests for run the testing.

Run tests:

```shell
pytest

# OR
make test
```

## Reference

- FastAPI: https://fastapi.tiangolo.com/
- PyTest: https://docs.pytest.org/en/7.1.x/
