def announce(f):
    def wrapper():
        print("Loading....")
        f()
        print("finish Downloading!!")
    return wrapper

@announce
def Downloader():   
    print("Files Downloading....")

Downloader()