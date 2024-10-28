from pypdf import PdfWriter
import argparse
from pathlib import Path

config = {
    'prog': 'pdftool',
    'description': 'It is a pdftool. Type -h/--help to view options',
    'epilog': 'testing'
}

parser = argparse.ArgumentParser(**config)
# parser.add_argument('-s','--source', nargs=1)
# parser.add_argument('-d','--dest', nargs=1)
parser.add_argument('-p','--pdf', nargs='+')
parser.add_argument('-P','--position', nargs='*')

args = parser.parse_args()

class Argment():
    
    error=''
    src_exist=False
    dest_exist=False



    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.check_source()
        self.check_dest()
    
    def get_property(self):
        source, dest = self.source, self.dest
        return [source, dest]


    def check_dest(self):

        if self.dest == None:
            self.error='No destination folder provided.'
            self.dest_exist = False
            parser.error(self.error)
            return

        dest_path = Path(self.dest)

        if not dest_path.exists():
            self.error='Destination pdf file does not exist.'
            self.dest_exist = False
            parser.error(self.error)
            return
        
        self.dest_exist = True

    def check_source(self):
        # print(self.__source)
        if self.source == None:
            self.error='No source folder provided.'
            self.src_exist = False
            parser.error(self.error)
            return

        source_path = Path(self.source)


        
        if not source_path.exists():
            self.error='Source pdf file does not exist.'
            self.src_exist = False
            parser.error(self.error)
            return

        self.src_exist = True
    


class PDF(Argment):

    filetype='.pdf'
    is_src_pdf = False
    is_dest_pdf = False
    

    def __init__(self, srcpdf, destpdf):
        super().__init__(srcpdf, destpdf)

        self.check_src_pdf()
        self.check_dest_pdf()

    def check_src_pdf(self, p:str='Source'):
        if not self.source.endswith(self.filetype):
            self.error=f'{p} {self.source} is not a {self.filetype}'
            self.is_src_pdf = False
            parser.error(self.error)
            return
        self.is_src_pdf=True

    def check_dest_pdf(self, p:str='Destination'):
        if not self.dest.endswith(self.filetype):
            self.error=f'{p} {self.dest} is not a {self.filetype}'
            self.is_dest_pdf = False
            parser.error(self.error)
            return
        self.is_dest_pdf=True



def main():

    # pdf = PDF(args.source if args.source == None else args.source[0], args.dest if args.dest == None else args.dest[0])
    
    # print(pdf.source, pdf.dest)
    print(args)



if __name__ == '__main__':

    main()