# coding=UTF-8
import re
from bs4 import BeautifulSoup
from urllib import parse
import urllib.request
import os

class HtmlParser(object):

    def parse(self, html_cont):

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        res_data = {}


        title_node = soup.find(id='dic')
        print(title_node)


        return title_node



