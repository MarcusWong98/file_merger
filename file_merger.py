import hashlib
import os
import argparse
from pathlib import Path
import shutil



parser = argparse.ArgumentParser(
    prog='file_merger',
    description='This program is to merge files from source folder to destination folder. Use -h to see more on how to use it.',
    epilog='testing'
)

default_source=str(Path('C:\\windows').resolve())
# print('default_source_str')
# print(default_source)


parser.add_argument('-s', '--source', nargs=1, default=default_source)
parser.add_argument('-d', '--dest', nargs=1)

args = parser.parse_args()

#############################################
class Argment():
    
    error=''


    def set_property(self, source, dest):
        self.__source = source
        self.__dest = dest
        self.check_source()
        self.check_dest()
    
    def get_property(self):
        source, dest = self.__source, self.__dest
        return [source, dest]
    
    def check_dest(self):
        # print(self.__dest)

        if self.__dest == None:
            self.error='No destination folder provided.'
            parser.error(self.error)
            return
        dest_path = Path(self.__dest)

        if not dest_path.exists():
            self.error='Destination folder does not exist.'
            parser.error(self.error)
            return        
        if not dest_path.is_dir():
            self.error='Destination provided is not a folder.'
            parser.error(self.error)
            return
        
        # self.__dest = dest_path

    def check_source(self):
        print(self.__source)
        if self.__source == None:
            self.error='No source folder provided.'
            parser.error(self.error)
            return
        source_path = Path(self.__source)

        if not source_path.exists():
            self.error='Source folder does not exist.'
            parser.error(self.error)
            return        
        if not source_path.is_dir():
            self.error='source provided is not a folder.'
            parser.error(self.error)
            return
        
        # self.__source = source_path
        

        


def hashfile(fname, chunk_size=1024):
    """
    Function which takes a file name and returns md5 checksum of the file
    """
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        # Read the 1st block of the file
        chunk = f.read(chunk_size)
        print('1st')
        # Keep reading the file until the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)
            print('reading...')

    # Return the hex checksum
    return hash.hexdigest()
    



def compare_file(file1, file2):
    
    hash1 = hashfile(file1)
    hash2 = hashfile(file2)
    print(hash1)
    print(hash2)

    if not hash1 == hash2:
        print('Different')
        return
    
    print('Same')

def main(args: Argment):
    
    source, dest = args.get_property()

    os.chdir(source)
    for file in os.listdir():
        print(file)
        shutil.copy2(file, 'C:/geservice')
    
    # for file in source.iterdir():
    #     print(file)
    #     print(type(file))
        
    #     shutil.copy(file, 'C:\projects\cli\\file_merger\\folder\\testfolder\\')

    print(type(source))
    print(type(dest))

    print('main')


if __name__ == '__main__':

    argment = Argment()
    argment.set_property(args.source if type(args.source)==str else args.source[0], args.dest if args.dest == None else args.dest[0])
    main(argment)

