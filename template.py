import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'research/trials.ipynb',
    'requirements.txt',
    'app.py',
]

for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass
        logging.info(f"creating file: {file_path}")

    else:
        logging.info(f"{filename} already exists.")    


