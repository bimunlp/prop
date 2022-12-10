import urllib.request
import tarfile
import os

folder_path = os.path.dirname(os.path.realpath(__file__))
print('Begin downloading of dataset')

dataset = 'ptc-corpus.tgz'
server = 'https://propaganda.qcri.org/ptc/data/'

print('downloading', dataset)
url = server + dataset
dataset_path = os.path.join(folder_path, dataset)
urllib.request.urlretrieve(url, dataset_path)

print('extracting', dataset)
with tarfile.open(dataset_path, 'r') as tar_file:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar_file, folder_path)
os.remove(dataset_path)