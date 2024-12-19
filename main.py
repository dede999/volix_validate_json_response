from typing import Optional

from fastapi import FastAPI, UploadFile, status, Response, Form, File

from infrastucture.exceptions.non_existing_platform import NonExistingPlatformException
from infrastucture.setup_verification import Setup
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/validate", status_code=status.HTTP_200_OK)
async def validate_map_data(response: Response,lines: int = Form(...),
                            ean_key: Optional[str] = Form(...), file: UploadFile = File(...)):
    lines_to_test, file_name = Setup.initialize_process(lines, file)

    try:
        result = await DataValidator(lines_to_test, file_name, ean_key).test_runner()
        return { "result": result }

    except NonExistingPlatformException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": str(e) }
