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

#### Example with response

```shell
curl --location --request POST 'https://volix-validate-json-response.onrender.com/validate' \                                                                                            ──(Thu,Jan02)─┘
--form 'file=@"/Users/andre_luiz/PycharmProjects/volix-scrapings/collect/santil/andra/santil_andra_2024-12-24-10.json"' \
--form 'lines="50"' \
--form 'ean_key="sku"' | json_pp
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5806    0  2245  100  3561    318    505  0:00:07  0:00:07 --:--:--   567
{
   "result" : {
      "both_fail" : [],
      "both_fail_count" : 0,
      "error_count" : 0,
      "errors" : [],
      "full_match" : [
         {
            "ean" : "7891040004416",
            "link" : "https://www.andra.com.br//fita-isolante-19mmx20mt-preta-3m/p",
            "price" : 28,
            "product_name" : "Fita Isolante 19Mmx20Mt Preta 33+ 3M ",
            "test_name" : "Fita Isolante 19Mmx20Mt Preta 33+ 3M ",
            "test_price" : 28
         },
         {
            "ean" : "7891040105502",
            "link" : "https://www.andra.com.br//fita-isolante-18mmx20mt-preta-imperial-slim-3m/p",
            "price" : 8.11,
            "product_name" : "Fita Isolante 18Mmx20Mt Preta 0,13Mm Imperial Slim 3M ",
            "test_name" : "Fita Isolante 18Mmx20Mt Preta 0,13Mm Imperial Slim 3M ",
            "test_price" : 8.11
         },
         {
            "ean" : "7891040014149",
            "link" : "https://www.andra.com.br//fita-isolante-19mmx10mt-autofusao-23br-3m/p",
            "price" : 32.76,
            "product_name" : "Fita Isolante 19Mmx10Mt AutofusÃ£o 23Br 3M ",
            "test_name" : "Fita Isolante 19Mmx10Mt AutofusÃ£o 23Br 3M ",
            "test_price" : 32.76
         },
         {
            "ean" : "7891040246809",
            "link" : "https://www.andra.com.br//lubrificante-para-puxamamento-de-cabos-500ml-3m/p",
            "price" : 26.27,
            "product_name" : "Lubrificante Para Puxamamento De Cabos 500Ml 3M ",
            "test_name" : "Lubrificante Para Puxamamento De Cabos 500Ml 3M ",
            "test_price" : 26.27
         },
         {
            "ean" : "7891040002917",
            "link" : "https://www.andra.com.br//fita-isolante-19mmx20mt-preta-highland-3m/p",
            "price" : 20.27,
            "product_name" : "Fita Isolante 19Mmx20Mt Preta Highland 3M ",
            "test_name" : "Fita Isolante 19Mmx20Mt Preta Highland 3M ",
            "test_price" : 20.27
         },
         {
            "ean" : "7891040216376",
            "link" : "https://www.andra.com.br//fita-crepe-48mm-50-metros-101la-3m/p",
            "price" : 13.84,
            "product_name" : "Fita Crepe 48Mm 50 Metros 101La 3M ",
            "test_name" : "Fita Crepe 48Mm 50 Metros 101La 3M ",
            "test_price" : 13.84
         },
         {
            "ean" : "7891040212835",
            "link" : "https://www.andra.com.br//fita-isolante-18mmx20mt-branca-imperial-3m/p",
            "price" : 10.26,
            "product_name" : "Fita Isolante 18Mmx20Mt Branca 0,13Mm Imperial 3M ",
            "test_name" : "Fita Isolante 18Mmx20Mt Branca 0,13Mm Imperial 3M ",
            "test_price" : 10.26
         },
         {
            "ean" : "7891040224746",
            "link" : "https://www.andra.com.br//fita-dupla-face-19mm-5-metros-4910-vhb-3m/p",
            "price" : 33.41,
            "product_name" : "Fita Dupla Face 19Mm 5 Metros 4910 Vhb 3M ",
            "test_name" : "Fita Dupla Face 19Mm 5 Metros 4910 Vhb 3M ",
            "test_price" : 33.41
         }
      ],
      "full_match_count" : 8,
      "name_fail" : [],
      "name_fail_count" : 0,
      "price_fail" : [],
      "price_fail_count" : 0,
      "total_count" : 8
   }
}
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