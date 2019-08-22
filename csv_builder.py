import csv
import os
def csv_create(comp_name, data, RESULT_FIELDS):
    """Creates a csv file that corresponds to the data of patents parsed
    
    Parameters
    ----------
    comp_name : str 
        Name of company parsed
    data : json 
        List of company and patent information
    RESULT_FIELDS : list 
        List of fields as rows for csv file
        
    Return
    ------
    attr : dict
        List pairing of file name and file path for later
        
    """
    
    #Build file name
    file_name = "PATENTS.csv"
    if comp_name != "":
        file_name = comp_name.upper() + " " + file_name  

    print("Building CSV file...")

    #Build file path
    dir_path = os.path.dirname(os.path.realpath("__file__")) + "\\CSV_Files\\"
        
    if os.path.exists(dir_path) == False:
        os.mkdir("CSV_FILES")
        
    file_path = dir_path + file_name

    #Open a new .csv file and fill in corresponding information
    with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, RESULT_FIELDS)
        writer.writeheader()  #Write the coloum header

        #Fill in each row with individual patent info
        for patent in data['patents']:
            writer.writerow(patent)

    print("Completed\n\nFile location: ", file_path)

    attr = {"name": file_name, "path": file_path}

    os.startfile(dir_path)
    
    return attr