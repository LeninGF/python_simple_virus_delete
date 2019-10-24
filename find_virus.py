import os
import re

dir_root = os.getcwd()
dir_target = os.path.join(dir_root, 'example_folder')
file_list = os.listdir(dir_target)
print('Files in folder {}:\n{}'.format(dir_target, file_list))

regex = r"[\w\d]+\.url"
matches = [re.findall(regex, x, re.MULTILINE) for x in file_list]
print(matches)
full_target = []
for match_vector in matches:
    for match_name in match_vector:
        file_root = os.path.join(dir_target, match_name)
        full_target.append(file_root)
        print(file_root)

# Now we the path to suspicious files all we have to do is delete