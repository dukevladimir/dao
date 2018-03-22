import os
import sys
import json

NAME = "Dune"
VERSION = "0.01"
CONFIG_FILE = "./config-file.json"
NODE_LIST = "./node-list.json"

def load_json(path):
	return json.load(open(path))

class node:

	def __init__(config = None, nodes = None):
		
		if config is not None:
			self._config = config
		else:
			# create config file
			pass

		if nodes is not None:
			self._nodes = nodes
		else:
			# create nodes file
			pass

	def handler(input):

		if input == 'help':
			pass
		else:
			pass


def main():
	print(">> starting {} p2p node - version {}".format(NAME,VERSION))
	print(">> searching for config-file in location '{}'".format(CONFIG_FILE))
	if os.path.isfile(CONFIG_FILE):
		config = load_json(CONFIG_FILE)
		print(">> importing config-file")
	else:
		config = None
		print(">> config-file not found")
	
	print(">> searching for node-list file in location '{}'".format(NODE_LIST))
	if os.path.isfile(NODE_LIST):
		nodes = load_json(NODE_LIST)
		print(">> importing node-list")
	else:
		nodes = None
		print(">> node-list not found")

	# create node object
	my_node = node(config,nodes)

if __name__ == '__main__':
	main()