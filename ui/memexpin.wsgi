import sys
import os
server_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, server_path)
sys.path.append(os.path.realpath(os.path.join(server_path, "../")))
from server import app as application
