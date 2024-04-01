from signLanguage.logger import logging
from signLanguage.exception import SignException
try:
    a = 5
    b = 0
    c = a/b
except SignException as e:
    print(e)