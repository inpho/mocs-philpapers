import xml.etree.ElementTree as ET

"""
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)

<a>
  <b />
  <c>
    <d />
  </c>
</a>
"""

root = ET.Element('dblp')
article = ET.SubElement(root, 'article')

"""
This should be generic, should iterate over the json dictionary 
and use the xmlmap to get the attribute name and the value.

To iterate over a dictionary, you use the dict.iteritems() function.
for key, value in DICT:
"""
ET.SubElement(article, 'author').text = "Pierre Marquis"

# print the tree
ET.dump(root)
