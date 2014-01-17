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


