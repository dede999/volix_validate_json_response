import json
import os
from typing import Optional

import uvicorn
from fastapi import FastAPI, UploadFile, status, Response, Form, File

from infrastructure.exceptions.invalid_validation_key import InvalidValidationKey
from infrastructure.exceptions.non_existing_platform import NonExistingPlatformException
from infrastructure.setup_verification import SetupVerification
from infrastructure.validation_config import ValidationConfig
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/validate", status_code=status.HTTP_200_OK)
async def validate_map_data(response: Response, ean_key: Optional[str] = Form(...), file: UploadFile = File(...)):
    file_content = file.file.read().decode("utf-8")
    valid_lines = SetupVerification.select_valid_lines(json.loads(file_content))

    try:
        config = ValidationConfig(valid_lines[0], ean_key, file.filename)
        platform_lines = config.platform.get_validation_instances_count()
        lines_to_test = SetupVerification.probabilistic_line_selection(valid_lines, platform_lines)
        result = await DataValidator(lines_to_test, config).test_runner()
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