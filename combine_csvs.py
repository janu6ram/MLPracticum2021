import os
import pandas as pd
import glob

# This is the path where you want to search
path = "/home/ramgadde/Desktop/MLPracticum2021/input"

# this is the extension you want to detect
extension = ".csv"

os.chdir(path)


all_files = []
dict1 = {}
for root_path,dirc, files_list in os.walk(os.getcwd()):
    #print(files_list)
    for a in files_list:
        b = str(a)
        if b.endswith(extension):
            print(root_path)
            file_path = str(root_path) + "/" + b
            data = pd.read_csv(file_path, error_bad_lines=False)
            print(data.shape)
            if path not in dict1:
                dict1[b] = data.shape
            all_files.append(data)


combined_csv = pd.concat(all_files)
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
print(dict1)            
print(combined_csv.shape) 



# os.chdir( path )
# result = glob.glob( '*/**.csv' )
# print( result )
# for root, dirs_list, files_list in os.walk(path):
#     for file_name in files_list:
#         print("hai")
#         if os.path.splitext(file_name)[-1] == extension:
#             file_name_path = os.path.join(root, file_name)
#             print(file_name)
#             print(file_name_path)   # This is the full path of the filter file

# directory = os.path.join("",".csv")
# print(directory)
# for root,dirs,files in os.walk(directory):
#     for file in files:
#         if file.endswith(".csv"):
#            #f=open(file, 'r')
#            #  perform calculation
#            pd.read_csv(f)
#            print(pd.head())
#            #f.close()

# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')