#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
def my_func(client):
    if len(sys.argv) > 1:
	    # Get address from command line
	    address = ' '.join(get_add.split('+'))
    else:
	    # Get address from clipboard
	    address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)
	
def test_it(args):
    print(args)
    my_func(args)

if __name__ == '__main__':
    client = input("Hi! Please add any address you want to see on map: ")
    test_it(client)
