import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, f"/var/www/Flask_selfedu")

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

activate_this='/usr/local/venvs/Flask_selfedu-Sj_JfD7p/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from main import app as application
