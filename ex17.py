from sys import argv
from os.path import exists

script,from_file,to_file = argv

open(from_file) ; print(f"The input file is {len(from_file)} bytes long") ; print(f"Does the output file exist? {exists(to_file)}") ; out_file = open(to_file, 'w') ; out_file.write(from_file) ; out_file.close()
