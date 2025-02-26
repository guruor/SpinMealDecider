# Development Instructions

## Prerequisites

Before setting up the project locally, ensure you have the following:

1. **Google Sheet Setup:**

   - Create a public Google Sheet.
   - Include a sheet for each meal: `Breakfast`, `Lunch`, `Dinner`.
   - Ensure each sheet has the following columns: `label`, `weight`.

2. **Dub.sh Setup:**
   - Create custom URLs for each meal in `dub.sh`.
   - Obtain the link IDs for each meal URL. These IDs will be required for the environment configuration.
   - Obtain the API key

## Environment Variables:

Copy .env.example to .env and fill in your specific configurations.

## Clone the Repository:

```bash
git clone https://github.com/guruor/SpinMealDecider.git
cd SpinMealDecider
```

## Local Setup (Without Docker)

### Requirements

- Python 3.7+
- Virtual Environment (Recommended: `venv`)
- pip

### Instructions

- Create and Activate Virtual Environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- Install Dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- Run the Application:

  ```bash
  python src/main.py
  ```

- Run Tests:

  ```bash
  python -m unittest discover -s src/test
  ```

## Docker Setup

- Build and Run Services:

  ```bash
  docker compose up --build
  ```

- Run Tests in Docker:

  ```bash
  docker compose run mealprocessor python -m unittest discover -s src/test
  ```
