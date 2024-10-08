import sys
import xml.etree.ElementTree as etree

# sum = 0
def get_attr_number(node):
    sum = len(node.attrib)
    
    for tag in node:
        sum += get_attr_number(tag)
        
    return(sum)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
