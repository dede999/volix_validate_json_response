import json
import numpy as np
from fastapi import UploadFile

PRODUCTS_TO_CHECK = 20

class Setup:
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

    @staticmethod
    def initialize_process(lines: int, file: UploadFile):
        file_content = file.file.read()
        json_ctt = Setup.filter_errors(json.loads(file_content))
        return Setup.select_test_lines(json_ctt, lines), file.filename
