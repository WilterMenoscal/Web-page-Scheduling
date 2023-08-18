import os
from pathlib import Path
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
print()
os.path.join(BASE_DIR, "static")
print(BASE_DIR)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    
]
print(STATICFILES_DIRS)