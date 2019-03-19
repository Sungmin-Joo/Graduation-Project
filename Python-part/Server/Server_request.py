import urllib.request

if __name__ == "__main__":
    print('Func_called - main')
    req = urllib.request.Request("http://http://192.168.35.132:5000/")
    data = urllib.request.urlopen(req).read() # data = urllib.requset.urlopen("http://www.daum.net").read()
    print(data)    
else:
    print('Func_called - imported')