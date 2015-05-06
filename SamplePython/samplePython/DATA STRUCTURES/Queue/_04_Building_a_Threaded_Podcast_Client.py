"""
he source code for the podcasting client in this section demonstrates how to use the
Queue class with multiple threads. The program reads one or more RSS feeds, queues
up the enclosures for the five most recent episodes to be downloaded, and processes
several downloads in parallel using threads. It does not have enough error handling for
production use, but the skeleton implementation provides an example of how to use the
Queue module.

First, some operating parameters are established. Normally, these would come
from user inputs (preferences, a database, etc.). The example uses hard-coded values
for the number of threads and a list of URLs to fetch.
"""

from Queue import Queue
from threading import Thread
import time
import urllib
import urlparse
import feedparser
# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()
# A real app wouldn't use hard-coded data...
feed_urls = [ 'http://advocacy.python.org/podcasts/littlebit.rss',]