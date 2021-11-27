import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = input("url: ")   #http://py4e-data.dr-chuck.net/comments_42.xml
xm = urlopen(url1, context=ctx).read()
tree = ET.fromstring(xm)

sum = 0
counts = tree.findall('.//count')
for node in counts:
    sum += int(node.text)
print(sum)
