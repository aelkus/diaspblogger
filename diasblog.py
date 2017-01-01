import diaspy 
import configparser
import sys 
import os 

def login(diaspPod, diaspUsername, diaspPassword, editCommand, postDirectory):
	"""Takes the user credentials and the name of the editor to 
	use as input (all strings) and connects to diaspora using 
	stream and connection objects. Prompts user for string inputs
	for either writing a post using the editor, importing a post
	in .txt format, or quitting. 
	"""
	c = diaspy.connection.Connection(pod=diaspPod,
								 username=diaspUsername,
								 password=diaspPassword)
	c.login()
	stream = diaspy.streams.Stream(c)
	ans = input("write a post, import a post, or quit? w/i/q: ")
	if ans == 'w': 
		writePost(stream, postDirectory, editCommand)
	elif ans == 'i': 
		importPost(stream, postDirectory)
	else: 
		sys.exit()

def importPost(stream, postDirectory): 
	"""Takes the stream object and post directory as input and 
	prompts user for name of the post. If the post exists in the 
	post directory, it will open it and then convert it into a 
	multi-line string. The string is then posted to user's 
	Diaspora pod, which renders any Markdown formatting through 
	the Diaspora pod. The function then revists the start menu. 
	"""
	fname = postDirectory + input("please enter name of your post: ")
	with open(fname) as file: 
		postStr="".join(line for line in file)
	stream.post(postStr)
	start() 
	
def writePost(stream, postDirectory, editCommand):
	"""Takes the stream object, post directory, and the editor command 
	as input and prompts user for the name of the post. This writes a new 
	.txt file to the post directory using the editor that the user 
	has configured. When the post is done, the user exits the editor 
	and the .txt file is opened and converted into a multi-line string. 
	The string is then posted to user's Diaspora pod, which renders 
	any Markdown formatting through the Diaspora pod. The function then
	revisits the start menu. 
	"""
	fname = postDirectory + input("please enter name of your post: ")
	fcommand = editCommand + " " + fname 
	os.system(fcommand)
	with open(fname) as file: 
		postStr="".join(line for line in file)
	stream.post(postStr) 
	start()

def start(): 
	"""Prompts user for a decision about whether or not to login. 
	If so, the function loads the configuration file and parses five 
	fields: 

	1. The name of the user's diaspora pod 
	2. The user's username for that diaspora pod 
	3. The user's password for the diaspora pod 
	4. The user's preferred editor for writing posts 
	5. The directory to write post .txt files to or load .txt files from 

	The login function is called with all of these inputs. If the user 
	opts to quit, the function exits the script. 

	"""
	ans = input("login? y/n: ")
	if ans == "n":
		sys.exit() 
	cfg = configparser.ConfigParser() 
	cfg.read('cfg.ini')
	if 'USERINFO' in cfg: 
		diaspPod = cfg['USERINFO']['diaspPod']
		diaspUsername = cfg['USERINFO']['diaspUsername']
		diaspPassword = cfg['USERINFO']['diaspPassword']
		editCommand = cfg['USERINFO']['editCommand']
		postDirectory = cfg['USERINFO']['postDirectory']
		login(diaspPod, diaspUsername, diaspPassword, editCommand, postDirectory)
	else: 
		sys.exit()

if __name__ == '__main__': 
	start() 