#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
def my_func(get_add):
    if len(sys.argv) > 1:
	    # Get address from command line
	    address = ' '.join(get_add)
    else:
	    # Get address from clipboard
	    address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)
	
def test_it(args):
	print(args[1:])
	my_func(args[1:])

if __name__ == '__main__':
	test_it(sys.argv)
	