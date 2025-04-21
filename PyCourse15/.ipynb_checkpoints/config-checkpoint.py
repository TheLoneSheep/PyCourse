from enum import Enum

token = '8172145152:AAGXu1bgUuUyt8laGeZwGgR6iob4azgkFVE'
db_file = 'database.vdb'


class States(Enum):
    S_START = "1"
    S_ENTER_DAY = "2"
    S_COUNTRY_OR_REGION = "3"
    S_ENTER_COUNTRY_OR_REGION = "4"
    S_ENTER_FIELDS_LIST = "5"
