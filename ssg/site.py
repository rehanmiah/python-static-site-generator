from pathlib import Path
class Site:
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)
    def create_dir(self,path):
        directory = self.dest / path.relative_to(self.source)
        mkdir(self.dest)


    def build(self):
        mkdir(self.dest)
        for j in self.source.rglob("*"):
            if j==dircetory:
                create_dir(j)




