from pathlib import Path
from typing import List
class Parser:
    extensions: List[str] = []
    def valid_extension(self,extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self,path):
        b = with open(path,r):
          return b.read()
    def write(self,path,dest,content,ext=".html"):
        full_path=dest / with_suffix(ext)
