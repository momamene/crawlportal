#!/usr/bin/env python
# coding: utf-8

from StringIO import StringIO
import pycurl
import re
import json
import sys
import urllib
from Queue import Queue

class Curller:

    def BFS(self, root_word):
        visit_table = {}
        visit_table[root_word] = 0
        curl = pycurl.Curl()
        queue = Queue()
        queue.put(root_word)
        while not queue.empty():
            storage = StringIO()
            base_word = queue.get()
            url = 'http://ac.search.naver.com/nx/ac?_callback=window.__jindo_callback._$3361_0&q=' + urllib.quote(base_word) + '&st=100'
            curl.setopt(curl.URL, url)
            curl.setopt(curl.WRITEFUNCTION, storage.write)
            curl.perform()
            #print url
            #print storage.buflist
            print base_word
            if len(storage.buflist) > 0:
                derivations = re.findall('(?<=\[")[^\]]+(?="\])', storage.buflist[0])
                for derivation in derivations:
                    if not derivation in visit_table:
                        visit_table[derivation] = visit_table[base_word] + 1
                        queue.put(derivation)
            else:
                print url
curller = Curller()

#root_word = raw_input()
root_word = '소녀시대'
curller.BFS(root_word)
