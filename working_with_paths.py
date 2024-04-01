# split file path, independent of the OS
# get normalized path
file_path = os.path.normpath(file_path)
# separate using the OS dependent separator
file_path_list = file_path.split(os.sep)
# or, in other words
file_path_list = os.path.normpath(file_path).split(os.sep)

# create file path from individual components
new_path = os.path.join(file_path_list[-4], file_path_list[-1])

# create folder if not present
if not os.path.exists("path/to/demo_folder"):
  os.makedirs("path/to/demo_folder")

# pip installations from local file, through a requirements txt file. an example.
fairseq @ file://C:/Users/user/fairseq

# check if local variable exists
if 'a_variable' in locals():
  return True
# check if global variable exists
if 'my_variable' in globals():
  return True

# add path to path variable
# useful to load modules from a specific path
sys.path.append('/path/to/module')


