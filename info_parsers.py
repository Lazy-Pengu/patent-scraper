import sys
import time

from csv_builder import csv_create

# TODO: Separate the request part and the data processing part
class InputParser:
    
    def __init__(self, data_obj, drive):
        self.comp_name = ""
        self.num = 10000
        self.year = ""
        self.data = None
        self.atr = {}

        self.compIn()
        self.numIn()
        self.yearIn()
        self.typeIn(data_obj)
        self.printIn()
        self.csvIn(data_obj)
        self.uploadIn(drive)
    
    def compIn(self):
        """Parses the name of company inputted by user
        
        Returns
        ------
        comp_name: str
            Name of company to parse for with no name resulting in search of all companies on database
            
        """
        self.comp_name = input("Enter Company Name (defualt=ALL): ")
        
    
    def numIn(self):
        """Parses the number of patents the user wants to find
        
        Raises
        ------
        ValueError
            Invalid number inputted
            
        Returns
        -------
        num : str
            Number of patents user want to get with no input resulting in search for max 10000
            
        """
        num_str = input("Enter number of patents want to retrieve (default=10000): ")
        try:
            if num_str != "":
                self.num = int(num)
        except ValueError:
            sys.exit("Invaild year inputted")
            
    def yearIn(self):
        """Start year user want start looking for patents from
        
        Raises
        ------
        ValueError
            Invalid number inputted
            
        Returns
        -------
        year : str
            Year to start parsing from with no input resulting in start year of 2007
            
        """
        self.year = input("Enter start year (default=2007): ")
        try:
            if self.year == "":
                self.year = "2007"
            else:
                int(self.year)
        except ValueError:
            sys.exit("Invaild year inputted")
            
    def typeIn(self, data_obj):
        """Parse the type of html request the user want to user
        
        """
        typ = input("GET or POST request type (default=GET): ")
        
        start_time = time.time()
            
        if typ != "" and typ != "GET" and typ != "POST":
            sys.exit("Invaild request type")
        elif typ == "" or typ == "GET":
            self.data = data_obj.getBuilder(self.comp_name, self.num, self.year)
        else:
            self.data = data_obj.postBuilder(self.comp_name, self.num, self.year)
            
        print("\nRequest Processing time: %s sec\n" % (time.time() - start_time))

    
    def csvIn(self, data_obj):
        if self.data['patents'] == None:
            print("\nCompany DNE or does not hold any related patents")
            return
        
        build = input("Create CSV file of the info [Y/n]: ")
        
        if build == "Y":
            self.atr = csv_create(self.comp_name, self.data, data_obj.RESULT_FIELDS)
        else:
            print("CSV skipped")
            
    
    def printIn(self):
        output = input("Print output [Y/n]: ")
    
        if output == "Y":
            print("\n", self.data)
        else:
            print("Print skipped")
            
    def uploadIn(self, drive):
        if self.atr == {}:
            print("Uploading skipped")
            return
        
        post = input("Upload file to Google Drive [Y/n] (Requires vaild credentials.json file): ")
        
        if post == "Y":
            service = drive.credentialVerification()
            drive.upload(service, self.atr['name'], self.atr['path'])
        else:
            print("File was not uploaded")
