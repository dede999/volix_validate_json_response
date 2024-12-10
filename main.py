import sys

from fastapi import FastAPI
from infrastucture.exceptions.non_existing_platform import NonExistingPlatformException
from infrastucture.setup_verification import Setup
from service.data_validator import DataValidator

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }
#     lines_to_test, file_name = Setup.initialize_process(sys.argv)
#
#     print("Number of lines to test: ", len(lines_to_test))
#
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