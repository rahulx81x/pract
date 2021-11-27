from urllib.request import urlopen
import ssl
import json

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = input("url: ") #http://py4e-data.dr-chuck.net/comments_42.json
JS = urlopen(url1, context=ctx).read()
js = json.loads(JS)

outp = 0
for i in js['comments']:
    outp += int(i['count'])
print(outp)
