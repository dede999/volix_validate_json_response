# Data Validation Application

This application is designed to validate data from various platforms using FastAPI. It processes uploaded files, validates the data, and returns the results.

## Features

- Validate data from different platforms
- Handle various exceptions and errors
- Return validation results in a structured format

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- aiohttp
- BeautifulSoup4
- Selenium
- Pytest
- UnitTest
- Other dependencies are listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dede999/volix_validate_json_response.git
    cd volix_validate_json_response
    ```

1. Install the dependencies:
    ```sh
      python bin/builder
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
      uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the API documentation.

## API Endpoints

- `GET /`: Returns a welcome message.
- `POST /validate`: Validates the uploaded file data.

### Necessary parameters

- `lines`: The number of lines to validate.
  - Type: `int`
  - If selected number of lines is greater than the number of lines in the file, the validation will be done for all lines.
- `ean_key`: The key to use for the EAN validation.
  - Type: `str` 
- `file`: The file to validate.
  - Type: `file`
  - Only JSON is supported.
  - The name of the file must follow the pattern: `platform_name_date_time.json`.
  - The data  must have the EAN key
  - The product name must be identified  by `product_name` or `product` key
  - The product price must be identified by `price`, `product_price` or `product_price` key

### Example Requests

#### Development Environment

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/validate' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'lines=10' \
  -F 'ean_key=some_key' \
  -F 'file=@path/to/your/file.csv' | json_pp
```

#### Production Environment
```shell
curl --location --request POST 'https://volix-validate-json-response.onrender.com/validate' \                                                                                         
--form 'file=@"/Users/andre_luiz/PycharmProjects/volix-scrapings/collect/santil/andra/santil_andra_2024-12-24-10.json"' \
--form 'lines="50"' \
--form 'ean_key="sku"' | json_pp
```

## Running Tests

### Run the unit tests:

```shell
pytest tests/unit
```

### Run the integration tests:

```shell
pytest tests/requests
```

## Project Structure

- `main.py`: The main FastAPI application.
- `service/`: Contains the core validation logic.
- `infrastructure/`: Contains setup and configuration files.
  - `exceptions/`: Contains custom exceptions.
- `tests/`: Contains tests for the application.
  - `unit/`: Contains unit tests.
  - `integration/`: Contains integration tests.

## Contributing

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.