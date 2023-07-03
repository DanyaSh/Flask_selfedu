
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, f"/var/www/{os.getenv('PRJ_NAME')}")

activate_this='{os.getenv("ENV_DIR")}'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from os.getenv("__MAIN__") import app as application
