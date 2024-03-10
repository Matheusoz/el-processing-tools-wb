
import bs4
import pandas as pd
import re
import requests
import subprocess
import tika
from bs4 import BeautifulSoup
from collections import Counter
from tika import parser
from typing import Union, List
# Make sure that a Tika service is running
# If tika is installed on a local machine, then just replace
# this with `http://localhost:9998`
TIKA_SERVER_ENDPOINT = 'http://tika:9998'