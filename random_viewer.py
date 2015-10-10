#!/usr/bin/env python

""" 

random_viewer.py 

This program downloads the list of viewers from a specified TwitchTV 
broadcaster's channel and selects a random viewer from the list.

TwitchTV sometimes returns an empty list of viewers which requires the the 
script to be re-run.

"""

# include dependencies
import ctypes, json, random, sys, urllib

def display(viewer):
  """ Displays the viewer's name in a message box. """
  
  # print viewer's username to CLI
  print "\nCongratulations! The winner is %s!" % viewer
  
  # display viewer's username with GUI
  ctypes.windll.user32.MessageBoxA(0, str(viewer), "The winner is... ", 0)

def download(username):
  """ Download and parse chatter information. """

  # create url with username
  url = "http://tmi.twitch.tv/group/user/" + username + "/chatters"
  
  # download raw chatters information
  data = urllib.urlopen(url).read()
  
  # parse data for the list of viewers
  if data.strip():
    data = json.loads(data)
  else:
    print "\nFailed to download data or data returned was empty.\n"
    print "data: ", data
    return False
  
  # return the list of viewers
  if data["chatter_count"]:
    return data["chatters"]["viewers"]
  else:
    print "\nNo chatters found.\n"
    return False
  
# main entry point
def main():

  # handle CLI arguments
  if not len(sys.argv) < 2:
    username = sys.argv[1]
  else:
    username = raw_input("TwitchTV Username: ")
  
  # call download and get list of viewers
  print "\nDownloading the list of viewers from %s\'s TwitchTV channel..." % username
  viewers = download(username)
  
  # check result of download
  if viewers:
    # display viewer count
    print "\nViewer count: %d\n" % len(viewers)
    # output each viewer
    for viewer in viewers:
      print viewer
    # display the lucky viewer
    display(random.choice(viewers))
  else:
    # exit on error
    return

# define main entry point
if __name__ == '__main__':
    main();

