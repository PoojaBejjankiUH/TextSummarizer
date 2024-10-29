import setuptools

with open("README.md", "r", encoding= "utf-8") as f :
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "PoojaBejjankiUH"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "pbejjanki@uh.edu"


setuptools.setup(
name=SRC_REPO,
version=__version__,
author=AUTHOR_USER_NAME,
author_email=AUTHOR_EMAIL,
description = "a simple package for nlp project",
long_description=long_description,
url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls = {
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

},

)