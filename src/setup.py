# settings.py
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / 'env.secret'
load_dotenv(dotenv_path=env_path)
