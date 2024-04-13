
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
import re
import enum
from typing import List
from datetime import date, datetime
from pydantic import BaseModel, Field, validator, AnyUrl
from hashlib import md5
from dateutil import parser

from wb_cleaning.types.metadata_enums import (
    WBAdminRegions,
    Corpus,
    WBDocTypes,
    WBGeographicRegions,
    WBMajorDocTypes,
    WBTopics,
    MajorDocTypes,
    RegionTypes,