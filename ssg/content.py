from collections.abc import Mapping
import re
from yaml import FullLoader, load

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)


    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm,Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data=metadata
        self.data["content"]=content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data:
            return None
        else:
        return self.data["type"]


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



