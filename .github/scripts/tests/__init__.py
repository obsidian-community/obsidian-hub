import os
import sys

# Add scripts/tests directory to path, so shared testing code is found
this_dir = os.path.dirname(__file__)
sys.path.insert(0,this_dir)

# Add scripts/ directory to path, so code in scripts/tests/ can import files from scripts/
parent_dir = os.path.dirname(this_dir)
sys.path.insert(0,parent_dir)
