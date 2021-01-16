from collections.abc import Mapping
import re
from yaml import FullLoader, load

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)


    def load(self, cls,string):
        __, fm, content=__regex.split(string,2)

    load(fm,Loader=FullLoader)
    cls(metadata, content)

class Content():
    def __init__(self, metadata, content):
        self.data=metadata
        self.data={"content":content}

    def __getitem__(self,key):
        return self.data[key]

    def __iter__(self):
        return self.data()

    def __len__(self):
        return self.data.length()

    def __rrepr__(self):
        data={}
        return str(data)
    for value in self.data.items():
        if key!="content":
            data[key]=value
"""
    @property:
    body():
    return self.data["content"]

    @propert:
    type():
    if self.data["type"] is not set:
        return None
    else:
        return self.data["type"]

    @property:
    type()
    self.data["type"]
"""



