from uuid import uuid4
import os

class FileUpload:
    def __init__(self,dir,perfix):
        self.dir=dir
        self.perfix=perfix
    
    def upload_to(self,instance,filename):
        name,ext=os.path.splitext(filename)
        return f'{self.dir}/{self.perfix}/{uuid4()}{ext}'