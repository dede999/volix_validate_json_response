import json
import sys
import numpy as np

from infrastucture import setup_verification
from request import carrefour_request_content

PRODUCTS_TO_CHECK = 150

async def main():
    file_name, products_count = setup_verification(sys.argv[1:])

    file_content = open(file_name).read()

    def has_no_error(line):
        return not "error" in line

    json_ctt = list(filter(has_no_error, json.loads(file_content)))
    line_count = len(json_ctt)

    prob = products_count / line_count

    # print(json_ctt)
    # print("Number of lines: ", line_count)
    # print("Probability: ", prob)

    lines_prob = np.random.rand(len(json_ctt)).tolist()
    lines_to_test = []

    for i in range(len(json_ctt)):
        if lines_prob[i] < prob:
            lines_to_test.append(json_ctt[i])
            
    # print("Number of lines to test: ", len(lines_to_test))
    url = "https://www.google.com"
    
    result = await carrefour_request_content(lines_to_test[0]["link"])
    print(result)
    return result

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


# for line in lines_to_test:
#     print(line)
#     print("\n")