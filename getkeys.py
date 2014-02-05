from glob import iglob as glob
import json
import os.path

data_path = "/var/inphosemantics/data/philpapers"

fields = set()
for filename in glob(os.path.join(data_path, "*.json")):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)

        # inserts any new kes that might appear
        fields.update(data.keys())

# print information to command line
for key in fields:
    print key
