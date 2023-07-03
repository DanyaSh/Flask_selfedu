
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, f"/var/www/{os.getenv('PRJ_NAME')}")

activate_this=f"{os.getenv('ENV_DIR')}"
print(activate_this)
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from main import app as application
