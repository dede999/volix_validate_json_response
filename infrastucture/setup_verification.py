import numpy as np


PRODUCTS_TO_CHECK = 20

class Setup:
    @staticmethod
    def setup_verification(argumets):
        if len(argumets) < 1:
            print("Usage: python3 main.py <file_name> <products_count (default = 20)>")
            return
        
        file_name = argumets[0]
        products_count = argumets[1] if len(argumets) == 2 else PRODUCTS_TO_CHECK
        
        return file_name, products_count
    
    @staticmethod
    def filter_errors(json_content):
        def has_no_error(line):
            return not "error" in line
        
        return list(filter(has_no_error, json_content))

    @staticmethod
    def select_test_lines(json_content, products_count):
        line_count = len(json_content)
        prob = products_count / line_count

        lines_prob = np.random.rand(len(json_content)).tolist()
        lines_to_test = []

        for i in range(len(json_content)):
            if lines_prob[i] < prob:
                lines_to_test.append(json_content[i])
                
        return lines_to_test
