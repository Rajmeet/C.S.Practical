import urllib
a = urllib.request.urlopen("https://www.pythonforbeginners.com/")
code = a.read() 
header = a.headers
info = a.info()

print(code, "\n", end = " ")
print(header, "\n", end = " ")
print(info,"\n", end = " ")


