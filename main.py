import os
from typing import Optional

import uvicorn
from fastapi import FastAPI, UploadFile, status, Response, Form, File

from infrastructure.exceptions.invalid_validation_key import InvalidValidationKey
from infrastructure.exceptions.non_existing_platform import NonExistingPlatformException
from infrastructure.setup_verification import SetupVerification
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/validate", status_code=status.HTTP_200_OK)
async def validate_map_data(response: Response,lines: int = Form(...),
                            ean_key: Optional[str] = Form(...), file: UploadFile = File(...)):
    lines_to_test, file_name = SetupVerification.initialize_process(lines, file)

    try:
        result = await DataValidator(lines_to_test, file_name, ean_key).test_runner()
        return { "result": result }

    except NonExistingPlatformException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": str(e) }

    except InvalidValidationKey as e:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return { "message": str(e) }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)