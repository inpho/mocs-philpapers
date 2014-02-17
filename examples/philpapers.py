'''The XML Schema for DBLP is located at dblp.uni-trier.de/xml/dblp.dtd'''

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
            xmlmap = make_map()
            genericElementTree(xmlmap,record)
            make_files(xmlmap, record)
   

def make_files(xmlmap, record):
    '''Takes the filenames, adds the XML extension, and creates a new file with that
    name, and adds the version header.'''
    
    filename = record['journal_or_collection_title'] + '.xml'
    target = open(filename, 'wb')
    target.write( '<?xml version="1.01"?>')
    target.write("\n\n")
    target.write(genericElementTree(xmlmap, record))

#builds a map from JSON fields to XML properties
def make_map():
    xmlmap = dict()
    xmlmap["journal_or_collection_title"] = "journal"
    xmlmap["title"] = "title"
    xmlmap["publication_year_or_status"] = "year"
    xmlmap["url"] = "url"
    xmlmap["pages"] = "pages"
    xmlmap["volume"]= "volume"
    xmlmap["school"]= "school"
    xmlmap["title"] = "title"
    xmlmap["authors"] = "LISTauthor"
    xmlmap["editors"] = "LISTeditor"
    xmlmap["publisher"] = "publisher"
    xmlmap["last_updated"] = "ATTRmdate"
    xmlmap["id"] = "ATTRkey"
    return xmlmap;

#given string "LASTNAME, FIRSTNAME", prints "FIRSTNAME LASTNAME"
def reorder(bname):
    switch=[1,0]
    nameaslist = bname.split(', ')
    nameaslist = [nameaslist[i] for i in switch]
    return ' '.join(nameaslist)

#iterates through a dictionary and uses the xmlmap to create an Element tree
def genericElementTree(xmlmap, record):
    root = ET.Element('dblp')
    article = ET.SubElement(root, 'article')
    for jsonkey, value in record.iteritems():
        try:
            tagname = xmlmap[jsonkey]
            keyname = xmlmap[jsonkey]
            if keyname.startswith("ATTR"):
                keyname=keyname[4:] #trim ATTR from keyname
                article.attrib[keyname]= value
            else:        
                if tagname.startswith("LIST"):
                    tagname = tagname[4:] # trim LIST from the tagname
                    for thing in value:
                        ET.SubElement(article,tagname).text = thing
                else:
                    ET.SubElement(article,tagname).text = value
        except KeyError:
            pass
 #   ET.dump(root)
    return ET.tostring(root)

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

