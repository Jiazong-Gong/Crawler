import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import csv


url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_1338728670'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
r = requests.get(url, headers=headers)
page = r.content.decode('utf-8')

