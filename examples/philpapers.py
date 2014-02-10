from glob import iglob as glob
import json
import os.path
import xml.etree.ElementTree as ET

def print_titles(data_path):
    ''' Takes a Philpapers data path, iterates through all JSON records in that
    folder, parses each and prints the title'''
    # search for all json files - the glob function iterates through a folder
    data_path = os.path.join(data_path, 'sample.json')
    for i,filename in enumerate(glob(data_path)):
        # open the file, parse the json, print the title, close the file
        with open(filename) as jsonfile:
            record = json.load(jsonfile)
     #       print record['journal_or_collection_title']
     #       make_files(record)
     #       print (str(record.keys()))
            xmlmap = make_map()
     #       for key in xmlmap.keys():
     #           print key
     #      elementTree()
            genericElementTree(xmlmap,record)
            
def make_files(record):
    '''Takes the filenames, adds the XML extension, and creates a new file with that
    name, and adds the version header.'''
    
    filename = record['journal_or_collection_title'] + '.xml'
    target = open(filename, 'wb')
    target.write( '<?xml version="1.01"?>')
    target.write("\n\n")
    target.write(record['title'])
    target.write("\n")

#builds a map from JSON fields to XML properties
def make_map():
    xmlmap = dict()
    xmlmap["journal_or_collection_title"] = "title"
    xmlmap["publication_year_or_status"] = "year"
    xmlmap["url"] = "url"
    xmlmap["pages"] = "pages"
    xmlmap["volume"]= "volume"
    xmlmap["school"]= "school"
#    xmlmap["authors"]="author"
    xmlmap["title"] = "title"
    
    return xmlmap;

#creates a manually assigned Element tree
def elementTree():
    root = ET.Element('dblp')
    article = ET.SubElement(root,'article')
    ET.SubElement(article,'author').text = "Pierre Marquis"
    ET.SubElement(article,'title').text = "Lost in translation: Language independence in propositional logic - application to belief change"
    ET.SubElement(article,'url').text =  "db/journals/ai/ai206.html#MarquisS14"
    ET.dump(root)

#iterates through a dictionary and use the xmlmap to create an Element tree
def genericElementTree(xmlmap, record):
    root = ET.Element('dblp')
    article = ET.SubElement(root, 'article')
    for jsonkey, value in record.iteritems():
        # elementname = xmlmap[jsonkey]
        # element = ET.SubElement(article,elementname)
        # element.text = value
        try:
            ET.SubElement(article,xmlmap[jsonkey]).text = value
        except KeyError:
            pass
       #ET.SubElement(article,key).text = value
    ET.dump(root)

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
#list all the keys for a particular file - done
#create a map that changes JSON fields to XML - in progress
#create a list of all possible tags for 400,000 files
#   keys lists all the tags for one file
#   return None if tag is not available
#write the xml code into file - working on
#save the file


