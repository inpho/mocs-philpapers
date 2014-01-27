from glob import iglob as glob
import json
import os.path

def print_titles(data_path):
    ''' Takes a Philpapers data path, iterates through all JSON records in that
    folder, parses each and prints the title'''
    # search for all json files - the glob function iterates through a folder
    data_path = os.path.join(data_path, '*.json')
    for i,filename in enumerate(glob(data_path)):
        # open the file, parse the json, print the title, close the file
        with open(filename) as jsonfile:
            record = json.load(jsonfile)
            print record['title']
            make_files(record)

def make_files(record):
    '''Takes the filenames, adds the XML extension, and creates a new file with that
    name, and adds the version header.'''
    
    filename = record['title'] + '.xml'
    target = open(filename, 'wb')
    target.write( '<?xml version="1.01"?>')
    target.write("\n\n")
    target.write(record['title'])


#def add_to_files(record):
#     '''Takes the json content and prints it onto the newly created file'''
#    pass



if __name__ == '__main__': 
    import sys
      
  # if a data path is manually specified, use it
    if sys.argv[-1] != 'philpapers.py':
        data_path = sys.argv[-1]
    else:
        # if not go with the inpho config file defaults
        # data_path = config.get('general', 'data_path')
        # philpapers_data_path = os.path.join(data_path, 'philpapers')
        pass
    print_titles(data_path)

#print file names of all json files - done
#create new file with filename + XML extension - done
#create a list of all possible tags for 400,000 files
#   keys lists all the tags for one file
#   return None if tag is not available
#write the xml code into file - working on
#save the file


