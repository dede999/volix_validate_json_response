from xmlrpc.client import DateTime


def print_file_content(line):
    timestamp = DateTime().now().timestamp()
    with open(f"out/{timestamp}_carrefour_orbia.csv", 'a', encoding='utf-8') as file:
        file.write(line)
        
async def carrefour_test_runner(products):
    for product in products:
        result = await carrefour_request_content(product["link"])
        expected_price = product["price"]
        print_file_content(f"{product['link']};{result['title']};{result['price']}\n")