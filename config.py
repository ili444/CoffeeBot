# -*- coding: utf-8 -*-
from enum import Enum

TOKEN = os.environ['token']
db_file = "database.vdb"


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_wait = "1"
    S_type_print = "2"
