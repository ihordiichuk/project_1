from django.shortcuts import render
from markdown2 import Markdown

from . import until

def convert_md_to_html(title):
    content = until.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

