# Hellviewer
It is a debugger for http sites, post and get query straight in you python code.

What it work?
```python
from hellviewer import show_debug_browser
show_debug_browser("<h1>Welcome to hell's debuger</h1>")
```
It's show a text in WebKit browser.
![showed](https://image.prntscr.com/image/g4wGMHaVTKqn8pZfcfkWWw.png "About screen")
If you want save and want walk in next link, you must include main site only this format "http://github.com"
```python
show_debug_browser("<h1>Welcome to hell's debuger in github. <a href='/TreeLoys'>Go</a></h1>", "http://github.com")
```
Where it use? In web scraper, bots, parsers web site for debug post,get requests and save information about site (just use BeutifullSoup and Requests).

I work above post and get sniffer (crazy pyqt5 api)


###This work on python 2.7 and pyqt5 (Anaconda). Other version not test.
