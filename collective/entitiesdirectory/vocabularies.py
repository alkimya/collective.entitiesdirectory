from xml.parsers import expat
from xml.dom import minidom

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

file = '/home/loc/iso3166.xml'


class Parser(object):
    """A class to parse XML file and extract character data"""
    
    def __init__(self):
        self.buff = []
        
    def charData(self, data):
        data = data.strip()
        if data:
            data = data.encode('utf8')
            self.buff.append(data)
            
    def parse(self, xml):
        parser = expat.ParserCreate()
        parser.CharacterDataHandler = self.charData
        parser.Parse(xml, 1)
        
def getCountries(context):
    """Return the list of the countries provide by the iso3166 XML file"""
    
    countries = []
    
    p = Parser()
    xmldoc = minidom.parse(file)
    nodes = xmldoc.childNodes
    
    list = nodes[1].getElementsByTagName("country")
    
    for e in list:
        elist = e.getElementsByTagName("country_name")
        for e in elist:
            p.parse(e.toxml())
            
    for country in sorted(p.buff):
        countries.append(SimpleTerm(country, country))

    return SimpleVocabulary(countries)