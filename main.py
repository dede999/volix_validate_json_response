import json
import sys
import numpy as np

from infrastucture.setup_verification import Setup
from request import carrefour_request_content

async def main():
    file_name, products_count = Setup.setup_verification(sys.argv[1:])

    file_content = open(file_name).read()

    json_ctt = Setup.filter_errors(json.loads(file_content))

    lines_to_test = Setup.select_test_lines(json_ctt, products_count)
            
    print("Number of lines to test: ", len(lines_to_test))
    
    result = await carrefour_request_content(lines_to_test[0]["link"])
    print(result)
    return result

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


# for line in lines_to_test:
#     print(line)
#     print("\n")