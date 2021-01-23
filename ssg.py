import sys
import typer
import ssg.parsers
from ssg.site import Site
def main(source="content",dest="dist"):
    config={"source":source,"dest":dest, "parsers":[ssg.parsers.ResourceParser(),ssg.parsers.MarkdownParser(),ssg.parsers.ReStructuredTextParser()]}
    Site(**config).build()
typer.run(main)

@staticmethod
def error(self, message):
    sys.stderr.write("\x1b[1;31m{}\n")