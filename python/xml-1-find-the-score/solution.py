import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = 0
    score += len(node.attrib)
    for i in node:
        score += get_attr_number(i) 
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
