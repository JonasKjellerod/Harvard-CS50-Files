from pyfiglet import Figlet
import sys
figlet = Figlet()
f = ['-f','--font']

if len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts() and sys.argv[1] in f :
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(input('Input: ')))
elif len(sys.argv) == 1:
    figlet.setFont(font = 'ansi_regular')
    print(figlet.renderText(input('Input: ')))
else:
    sys.exit('Invalid Usage')


