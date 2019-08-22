import json

class Query:
    """
    Holds the two query parameters for GET and POST request
    
    """

    def getParameter(self, comp_name, num_pat, start_date, result_fields):
        """Query parameter for GET request
        
        Parameters
        ----------
        comp_name : str
            Company name to parse
        num_pat : int
            Number of patents to parse
        start_date : str
            Year to start parsing patents
        
        Returns
        -------
        val : dict
            Completed query parameter to search for corresponding patents
        
        """
        query_parameters = {
      "_and": [
        {
          "_contains": {
            "assignee_organization": comp_name
          }
        },
        {
          "_gte": {
            "patent_date": start_date
          }
        },
        {
          "_or": [
            {
              "_text_phrase": {
                "patent_title": "autonomous vehicle"
              }
            },
            {
              "_text_phrase": {
                "patent_abstract": "autonomous vehicle"
              }
            },
            {
              "_text_phrase": {
                "patent_title": "self-driving car"
              }
            },
            {
              "_text_phrase": {
                "patent_abstract": "self-driving car"
              }
            },
            {
              "_text_phrase": {
                "patent_title": "autonomous vehicles"
              }
            },
            {
              "_text_phrase": {
                "patent_abstract": "autonomous vehicles"
              }
            },
            {
              "_text_phrase": {
                "patent_title": "automated vehicle"
              }
            },
            {
              "_text_phrase": {
                "patent_abstract": "automated vehicle"
              }
            },
            {
              "_text_phrase": {
                "patent_title": "autonomous driving"
              }
            },
            {
              "_text_phrase": {
                "patent_abstract": "automated driving"
              }
            }
          ]
        }
      ]
    }
        
        modify = {
            "per_page": num_pat
        }

        # Create json object using parameters
        q = json.dumps(query_parameters)
        f = json.dumps(result_fields)
        o = json.dumps(modify)

        # Bulid parameter objects
        val = {'q' : q, 'f' : f, 'o' : o}
        
        return val

    def postParameters(self, comp_name, num_pat, start_date, result_fields):
        """Query parameter for POST request
        
        Parameters
        ----------
        comp_name : str
            Company name to parse
        num_pat : int
            Number of patents to parse
        start_date : str
            Year to start parsing patents
        results_fields : list
            List of results to search for
            
        Returns
        -------
        query_parameters : dict
            Completed query parameter to search for corresponding patents
        
        """
        query_parameters = {
          "q": {
            "_and": [
              {
                "_contains": {
                  "assignee_organization": comp_name
                }
              },
              {
                "_gte": {
                  "patent_date": start_date
                }
              },
              {
                "_or": [
                  {
                    "_text_phrase": {
                      "patent_title": "autonomous vehicle"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_abstract": "autonomous vehicle"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_title": "self-driving car"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_abstract": "self-driving car"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_title": "autonomous vehicles"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_abstract": "autonomous vehicles"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_title": "automated vehicle"
                    }
                  },
                  {
                    "_text_phrase": {
                      "patent_abstract": "automated vehicles"
                    }
                  }             
                ]
              }
            ]
          },
          "f": result_fields,
          "o": {
            "per_page": num_pat
          }
        }

        return query_parameters
