import os
import sys

NAME = "Dune"
VERSION = "0.01"
CONFIG_FILE = "./config-file.json"
NODE_LIST = "./node-list.json"

class node:

	def __init__(config = None, nodes = None):
		
		if config is not None:
			self._config = config
		else:
			# create config file 


def main():
	print(">> starting {} p2p node - version {}".format(NAME,VERSION))
	print(">> searching for config-file in location '{}'".format(CONFIG_FILE))


if __name__ == '__main__':
	main()