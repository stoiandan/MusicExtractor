#!/bin/env python3


## Music extractor. Extracts all music files from a
## folder hierarchy to the root 


from sys import argv as args
from os import listdir, path as os_path
from shutil import copyfile

class Extractor:
    def __init__(self, *args):
        self.root = args[0]
        self.queue = []
        self.extensions = [".m4a",".mp3",".flac",".ogg",".wmw"]
        
        self.__init__queue()
        
    def __init__queue(self):
        for dr in listdir(self.root):
            dr = self.get_path(self.root,dr)
            if os_path.isdir(dr):
                self.queue.append(dr)
        

    def extract(self):
        for origin in self.queue:
            self.__extract_in_depth(origin)
            


    def __extract_in_depth(self, origin):
        for path in listdir(origin):
            path = self.get_path(origin, path)
            if self.is_music(path):
                copyfile(path, self.get_new_origin_path(path))
            elif os_path.isdir(path):
                self.__extract_in_depth(path)
        


    def get_path(self, first, second):
        return os_path.join(first,second)
    
    def get_new_origin_path(self, path):
        return self.get_path(self.root,os_path.basename(path))

    def is_music(self, file):
        for ex in self.extensions:
            if file.endswith(ex):
                return True

        return False
            
            
def main():
    if len(args) != 3:
        print("""Not enough arguments provided:
                -i input_path  """)
        return
    ex = Extractor(args[2])
    ex.extract()

if __name__ == "__main__":
    main()
