import os
import constant

count = 0
for folder_path in os.listdir(constant.PASSAGE_FOLDER):
    for filename in os.listdir(constant.PASSAGE_FOLDER + '/' + folder_path):
        with open(constant.PASSAGE_FOLDER + '/' + folder_path+'/'+filename, 'r') as f:
            length = len(f.read().split())
            if length > constant.PASSAGE_LENGTH_LIMIT:
                count += 1
                print(filename, length)
print(count)