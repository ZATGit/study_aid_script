try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'A study aid that pulls nouns and verbs from a webpage to create class & function questions',
    'author':'Zach Trembly',
    'url':'github.com/ZATGit',
    'download_url':'https://github.com/ZATGit/study_aid',
    'author_email':'mail@zachtrembly.com',
    'version':'0.3',
    'license':'MIT',
    'install_requires':[],
    'packages':['study_aid'],
    'scripts':[],
    'name':'Study Aid'
}

setup(**config)