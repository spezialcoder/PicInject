#/usr/bin/python3
import argparse, sys, os, zipfile, base64, random, imghdr, os
from colorama import Fore
import json
##Exceptions
class ObjectInitException(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return self.reason


class InjectorException(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return self.reason


##Injector
class PicInjectObject:
    def __init__(self, target, file=None, password=None):
        self.target = target
        self.file = file
        self.password = password
        self.ready = False
        self.mode = None

    def initObject(self):
        if os.path.isfile(self.target) and os.path.isfile(self.isNone(self.file)) and imghdr.what(self.target) != None:
            self.ready = True
            self.mode = 0

        elif os.path.isfile(self.target) and self.file is None and imghdr.what(self.target) != None:
            self.ready = True
            self.mode = 1

        else:
            self.ready = False
            raise ObjectInitException("Target or InjectFile not found")

    def check(self):
        if self.ready:
            with open(self.target, "rb") as file:
                content = file.read()
                file.close()

            content = content[content.find(b"bstart"):][6:]
            if len(content) > 0:
                return True

            else:
                return False

        else:
            raise InjectorException("Object not initialized")



    def inject(self):
        if self.ready and self.mode == 0:
            zipname = "tmp{0}.zip".format(random.randint(0,1000))
            newZip = zipfile.ZipFile("temp/{0}".format(zipname),"w")
            newZip.write(self.file)
            newZip.close()

            with open("temp/"+zipname, "rb") as file:
                content = file.read()
                file.close()
            os.remove("temp/"+zipname)
            with open(self.target, "ab") as file:
                print(content)
                file.write(b"bstart"+base64.encodebytes(content))
                file.close()
        else:
            raise InjectorException("Object not initialized or invalid mode")


    def extract(self):
        if self.ready and self.mode == 1:
            zipname = "tmp{0}.zip".format(random.randint(0, 1000))
            with open(self.target, "rb") as file:
                content = file.read()
                file.close()

            content = base64.decodebytes(content[content.find(b"bstart"):][6:])

            with open("temp/"+zipname, "wb") as file:
                file.write(content)
                file.close()

            os.mkdir("../result")
            newZip = zipfile.ZipFile("temp/"+zipname,"r")
            newZip.extractall("result/")
            os.remove("temp/"+zipname)

        else:
            raise InjectorException("Object not initialized or invalid mode")

    def isNone(self, var):
        if var is None:
            return ""

        else:
            return var

    def listToString(self,the_list):
        ret = b""
        for item in the_list:
            ret += item
        return ret


##Essential Methods
def printToConsole(text, kind):  # Kind 0: error #Kind 1 : progress #Kind 2 : Success
    if kind == 0:
        print(Fore.RED + "[-]" + Fore.RESET + text)

    elif kind == 1:
        print(Fore.YELLOW + "[*]" + Fore.RESET + text)

    elif kind == 2:
        print(Fore.GREEN + "[+]" + Fore.RESET + text)


def printLogo():
    pass


def getActualVersion():
    with open("../version.json", "r") as version_file:
        try:
            version = json.loads(version_file.readline())["version"]
            return version
        except:
            printToConsole("Failed to load version.json")
            return

def checkUpdates():
    pass

##Parser
parser = argparse.ArgumentParser(description='Hide files in images')
parser.add_argument('--target' ,type=str,help='The target file', required=True)
parser.add_argument("--file", type=str, help="The file to hide")
parser.add_argument("--inject", help="Hides a file in another file", action="store_true")
parser.add_argument("--extract", help="Extracts a file from an injected file" ,action="store_true")
parser.add_argument("--check", help="Checks if a file is injected", action="store_true")
parser.add_argument("--password", type=str, help="Adds a password")
parser.add_argument("--update", help="Update picinject")
args = parser.parse_args()


if args.check:
    inj = PicInjectObject(args.target)
    try:
        inj.initObject()
    except:
        printToConsole("Cant find target file",0)
        sys.exit()

    check_result = inj.check()
    if check_result:
        printToConsole("Target file is injected",2)

    elif not check_result:
        printToConsole("Target file is not injected",0)

elif args.inject:
    inj = PicInjectObject(args.target,args.file)
    try:
        inj.initObject()
    except:
        printToConsole("Cant find target file or file",0)
        sys.exit()

    if inj.check():
        printToConsole("File already injected",0)
    else:
        inj.inject()
        printToConsole("File injected",2)

elif args.extract:
    inj = PicInjectObject(args.target)
    try:
        inj.initObject()
    except:
        printToConsole("Cant find target file",0)
        sys.exit()

    if inj.check():
        inj.extract()
    else:
        printToConsole("Target file is not injected",0)

elif args.update:
    pass