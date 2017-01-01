# Diaspblogger

A simple command line tool for posting to the [Diaspora](https://diasporafoundation.org) microblogging network. Allows user to write or import `.txt` files and deploy them as posts to their Diaspora pod account. Written as a quick and dirty solution for blogging with Diaspora utilizing the `Diaspy` module. (Minimally) tested on macOS Sierra 10.12.2 with Python3 3.4.1 using `vim` or `sublime -w` as the editor configuration and `diasp.org` as the pod. The `.txt` file can be written with Markdown syntax, as Diaspora will render Markdown. However, I've only tested this with Markdown syntax for text (links, quotes, code blocks, etc) and not much else. 

## Dependencies

* [Python3](https://docs.python.org/3/) (at least 3.3) 
* [Diaspy](https://github.com/marekjm/diaspy) 

## Usage 

### Installation 

if you have the dependencies, clone this repository to a director of your choice. Next, `cd` into the repo and edit the `cfg.ini` file. 

* `diaspPod` should have the name of your Diaspora pod (for ex, https://diasp.org) ). 
* `diaspUsername` should have your Diaspora username (for ex, harambe, doge, or harambe_doge, etc). 
* `diaspPassword` should have your Diaspora password (for ex, honorTheLateHarambe). 
* `editCommand` should have your preferred editor (for ex, vim). 
* `postDirectory` should have the path to the directory you want to use for your posts (for ex, /Users/harambe/diaspora-blogging/posts/). 

### Startup

Next, run the command `python3 diasblog.py` to begin the script. It should prompt you to decide whether or not to log in with `login? y/n: `. Type `y` to log in and `n` to log out. Presuming you typed `y` it will then prompt you to decide whether or not to write a post, import a post, or quit: `write a post, import a post, or quit? w/i/q:`. 

### Writing Posts

Presuming you typed `w`, you'll be prompted to specify a name (`foo.txt`) for your file. Once you do so, the editor you specified will open to write the post (which will be saved to your post directory). When you are done with the post, exit the editor (for example, in vim type `wq`). Your text file will be read into a string and then posted to Diaspora. 

### Importing Posts 

Presuming you typed `i`, you will be prompted to specify the name of the `.txt` file you are to import from the post directory you specified earlier. This text file (`foo.txt`) is then read into a string and posted to Diaspora. 
