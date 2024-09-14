import sys

colors = True
machine = sys.platform  
if machine.lower().startswith(("os", "win", "darwin", "ios")):
    colors = False 

if not colors:
    reset = red = white = green = blue = yellow = ""
else:
    reset = "\033[0m"
    white = "\033[97m"
    black = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    gray = "\033[37m"
    dark_red = "\033[31m"
    dark_green = "\033[32m"
    dark_yellow = "\033[33m"
    dark_blue = "\033[34m"
    dark_magenta = "\033[35m"
    dark_cyan = "\033[36m"
    light_black = "\033[90m"
    light_red = "\033[91m"
    light_green = "\033[92m"
    light_yellow = "\033[93m"
    light_blue = "\033[94m"
    light_magenta = "\033[95m"
    light_cyan = "\033[96m"
    light_white = "\033[97m"
    background_black = "\033[40m"
    background_red = "\033[41m"
    background_green = "\033[42m"
    background_yellow = "\033[43m"
    background_blue = "\033[44m"
    background_magenta = "\033[45m"
    background_cyan = "\033[46m"
    background_white = "\033[47m"