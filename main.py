from typing import Optional

from fastapi import FastAPI, UploadFile, status, Response

from infrastucture.exceptions.non_existing_platform import NonExistingPlatformException
from infrastucture.setup_verification import Setup
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/validate", status_code=status.HTTP_200_OK)
async def validate_map_data(
        file: UploadFile, response: Response, lines: Optional[int] = 20,
        ean_key: Optional[str] = "ean"):
    lines_to_test, file_name = Setup.initialize_process(lines, file)

    try:
        result = await DataValidator(lines_to_test, file_name).test_runner(ean_key)
        return { "result": result }

    except NonExistingPlatformException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": str(e) }
