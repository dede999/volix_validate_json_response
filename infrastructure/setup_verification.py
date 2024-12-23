import json
import numpy as np
from fastapi import UploadFile

PRODUCTS_TO_CHECK = 20

class SetupVerification:
    @staticmethod
    def line_is_valid(line):
        return (not "error" in line) and ("link" in line)

    @staticmethod
    def filter_errors(json_content):
        return list(filter(SetupVerification.line_is_valid, json_content))

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
        json_ctt = SetupVerification.filter_errors(json.loads(file_content))
        return SetupVerification.select_test_lines(json_ctt, lines), file.filename
