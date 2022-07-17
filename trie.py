# importing the required modules
import os
import argparse
from pprint import pprint
from source import *



def amir(arg):
    print("helllo")
def read(args):
	print('hello word')


def show1(args):
	# get path to directory
	dir_path = args.show[0]
	
	# validate path


def delete(args):
	# get the file name/path
	file_name = args.delete[0]

	# validate the file name/path
	
	# delete the file
	os.remove(file_name)
	print("Successfully deleted {}.".format(file_name))
	

def copy(args):
	# file to be copied
	file1 = args.copy[0]
	# file to copy upon
	file2 = args.copy[1]

	# validate the file to be copied

	# validate the type of file 2
	print("Successfully copied {} to {}.".format(file1, file2))


def rename(args):
	old_filename = args.rename[0]

	new_filename = args.rename[1]


	os.rename(old_filename, new_filename)
	print("Successfully renamed {} to {}.".format(old_filename, new_filename))

parser = argparse.ArgumentParser(description = "a hard project ....")
parser.add_argument("-add", "--add", type = str, nargs = 1,
					metavar = "string", default = None,
					help = "add your string in trie")
parser.add_argument("-find", "--find", type = str, nargs = 1,
					metavar = "string", default = None,
					help = "search your string in trie.")
parser.add_argument("-delete", "--delete", type = str, nargs = 1,
					metavar = "string", default = None,
					help = "delete your string in trie.")



args = parser.parse_args()
if args.find != None:
	x=args
	print(t.search(x.find[0]))
elif args.add !=None:
	x=t.insert(args.add[0])
	if not x:
		print('baddddd')
	else:
		print('ok')
elif args.delete !=None:
	t.delete(args.delete[0])



