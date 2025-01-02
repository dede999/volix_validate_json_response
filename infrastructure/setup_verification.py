import json
import numpy as np
from fastapi import UploadFile

class SetupVerification:
    @staticmethod
    def line_is_valid(line):
        return (not "error" in line) and ("link" in line)

    @staticmethod
    def filter_errors(json_content):
        return list(filter(SetupVerification.line_is_valid, json_content))

    @staticmethod
    def probabilistic_line_selection(json_content, products_count):
        line_count = len(json_content)
        prob = products_count / line_count

        lines_prob = np.random.rand(len(json_content)).tolist()
        lines_to_test = []

        for i in range(len(json_content)):
            if lines_prob[i] < prob:
                lines_to_test.append(json_content[i])
                
        return lines_to_test
