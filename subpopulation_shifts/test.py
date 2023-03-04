import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..'))
print(parent_dir)
root_dir = os.path.join(parent_dir,'data')
print(root_dir)