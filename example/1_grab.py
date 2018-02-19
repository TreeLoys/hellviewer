#coding: utf8
#Autor: blackzero

#include after for import __init__.py script
import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
"""
The first look on www site zone,
Two look on user-agent, other version user-agent in you aim site
Three use requests as standard alone library for get static html(not use content)  
"""
#import hellviewer =)
from __init__ import show_debug_browser
from requests import get


if __name__ == "__main__":
	headers = {
		'User-Agent': 'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)'
	}
	raw = get("https://google.ru/", headers=headers)

	show_debug_browser(raw.text, "https://www.google.ru/")
