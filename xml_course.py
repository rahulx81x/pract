import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = input("url: ")
xml = urlopen(url1, context=ctx).read()
tree = ET.fromstring(xml)

sum = 0
counts = tree.findall('.//count')
for node in counts:
    sum += int(node.text)
print(sum)
