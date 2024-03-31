import pyshorteners

url = input("enter the url : ")

def shortnerurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortnerurl(url)    
