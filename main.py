import json
import sys
from typing import Optional

from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from infrastucture.exceptions.non_existing_platform import NonExistingPlatformException
from infrastucture.setup_verification import Setup
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/validate")
async def validate_map_data(file: UploadFile, lines: Optional[int] = 20):
    lines_to_test, file_name = Setup.initialize_process(lines, file)
    return { "lines": lines_to_test, "file": file_name, "lines_to_test": lines_to_test }
#     try:
#         await DataValidator(lines_to_test, file_name).test_runner()
#     except NonExistingPlatformException as e:
#         print(str(e))
#
#
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
#

# for line in lines_to_test:
#     print(line)
#     print("\n")