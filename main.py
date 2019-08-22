import sys
from uspto_request import HtmlRequest
from info_parsers import InputParser
from drive_uploader import Uploader

if __name__ == "__main__":
    data_obj = HtmlRequest()
    drive = Uploader()
    input_val = InputParser(data_obj, drive)

    
    print("\n***Program Completed***\n")