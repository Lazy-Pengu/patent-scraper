import json
#import csv
import requests
from bs4 import BeautifulSoup

from query_parameters import Query

class HtmlRequest:
    """
    Create an HTML request (GET and POST) with user parsed info using USPTO API
    
    """
    
    #Base url and query categories
    BASE_URL = "http://www.patentsview.org/api/patents/query"
    RESULT_FIELDS = ['patent_number', 'patent_date', 'patent_title', 'patent_abstract']
    
    def __init__(self):
        self.query = Query()  #Import query parameter for parsing

    def getBuilder(self, comp_name, num_pat=10000, start_year="2007"):
        """Get corresponding json data from GET request
        
        Parameters
        ----------
        comp_name : str
            Company name to parse
        num_pat : int
            Number of patents to parse
        start_year : str
            Year to start parsing patents
            
        Returns
        -------
        data : json
            Data from USPTO API for corresponding query parameter
        
        """
        
        start_date = start_year + "-01-01"  #Create full year
        
        parameters = self.query.getParameter(comp_name, num_pat, start_date, self.RESULT_FIELDS)
    
        print("Processing GET request...")
        
        # Create GET request and convert to json
        r = requests.get(self.BASE_URL, params=parameters)
        data = r.json()
        
        print("Completed GET request")
        
        return data
    
    def postBuilder(self, comp_name, num_pat=10000, start_year="2007"):
        """Get corresponding json data from POST request
        
        Parameters
        ----------
        comp_name : str
            Company name to parse
        num_pat : int
            Number of patents to parse
        start_year : str
            Year to start parsing patents
        
        Returns
        -------
        data : json
            Data from USPTO API for corresponding query parameter
            
        """
        
        start_date = start_year + "-01-01"  #Create full year
        
        query_parameters = self.query.postParameters(comp_name, num_pat, start_date, self.RESULT_FIELDS)
        
        # Create json object using parameters
        q = json.dumps(query_parameters)

        print("Processing POST request...")
        
        # Create POST request and convert to json
        r = requests.post(self.BASE_URL, data=q)
        data = r.json()
        
        print("Completed POST request")

        return data
    
