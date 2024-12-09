import sys

from infrastucture.setup_verification import Setup
from request import carrefour_request_content

async def main():
    lines_to_test, file_name = Setup.initialize_process(sys.argv)
            
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