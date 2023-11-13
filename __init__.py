"""
================== file_name : 'asciiTUI/__init__.py' ==================
======================= import_name : 'asciiTUI' =======================
                                                                        
Last Update: 12/11/2023 (GMT+7)                                         
                                                                        
Description: This is a library of tools for you to use with your needs  
               for an attractive type of terminal (console) display.    
                                                                        
Information: Type 'print(dir(asciiTUI))' for further functions, then    
                type 'print(asciiTUI.{func}.__doc__)' for further       
                      document information of each function             
"""

# -- importing: all: {time, os, re, sys, getpass}, add: {windows: {msvcrt} else: {tty, termios}} -- #
import time, os, re, sys, getpass
if sys.platform == 'win32':
  from msvcrt import getch
else:
  import tty, termios

# -- var(s) -- #
__version__  = '1.1.0'
__ansi_key   = {
  # - RESET - #
  "reset"     : "\033[0m",
  # - STYLE - #
  "bold"      : "\033[1m",
  "italic"    : "\033[3m",
  "underline" : "\033[4m",
  "strike"    : "\033[9m",
  # - COLOR - #
  "black"     : "\033[30m",
  "red"       : "\033[31m",
  "green"     : "\033[32m",
  "yellow"    : "\033[33m",
  "blue"      : "\033[34m",
  "magenta"   : "\033[35m",
  "cyan"      : "\033[36m",
  "white"     : "\033[37m",
  "orange"    : "\033[38;5;208m",
  "gray"      : "\033[90m",
  # - BACKGROUND COLOR  - #
  "bg_black"  : "\033[40m",
  "bg_red"    : "\033[41m",
  "bg_green"  : "\033[42m",
  "bg_yellow" : "\033[43m",
  "bg_blue"   : "\033[44m",
  "bg_magenta": "\033[45m",
  "bg_cyan"   : "\033[46m",
  "bg_white"  : "\033[47m",
  "bg_orange" : "\033[48;5;208m",
  "bg_gray"   : "\033[100m"
}
module_use   = r'{time, os, re, sys, getpass}, add: {windows: {msvcrt} else: {tty, termios}}'
lorem_ipsum  = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# -- class Error(s) -- #
class CodeStyleEmptyError(Exception):
  def __init__(self, *message):
    super().__init__(*message)

class OptionNotFoundError(Exception):
  def __init__(self, *message):
    super().__init__(*message)

class Python2VersionError(Exception):
  def __init__(self, *message):
    super().__init__(*message)

# -- Python version checking -- #
if sys.version_info[0] == 2:
  raise Python2VersionError("asciiTUI only works in python 3, not 2")

# -- func(s) -- #
# -- func: removing ansi code '\033' | return True -- #
def remove_ansi(text):
  """
return: True
asciiTUI.remove_ansi(text=str)

Args:
  text : The main text that will remove the ansi code \\033.
  """
  for code in __ansi_key.values():
    text = str(text).replace(code, "")
  ansi_escape_pattern = r'\033\[[0-9;]*[mK]'
  text = re.sub(ansi_escape_pattern, '', text)
  return text

# -- func: get terminal size | return True -- #
def terminal_size(get):
  """
return: True
asciiTUI.table(get=str)

Args:
  get : The type of terminal size you will get. 'x': width, 'y': height.
  """
  x, y = os.get_terminal_size().columns, os.get_terminal_size().lines
  if get.lower() == 'x':
    return x
  elif get.lower() == 'y':
    return y
  elif get.lower() == 'xy':
    return x, y
  elif get.lower() == 'yx':
    return y, x
  else:
    raise OptionNotFoundError(f"There is no type as '{get}'.")

# -- func: make color text terminal | return True -- #
def colored(text="colored(<Your text>, <color or style>)", style="white"):
  """
return: True
asciiTUI.colored(text=str, style=str)

Args:
  text  : Main string text to change the style type
  style : Selection of string text style <split: ','. Example: style='black, bg_black'>

Style Key(s):
{
  # - RESET - #
  "reset"
  # - STYLE - #
  "bold"
  "italic"
  "underline"
  "strike"
  # - COLOR - #
  "black"
  "red"
  "green"
  "yellow"
  "blue"
  "magenta"
  "cyan"
  "white"
  "orange"
  "gray"
  # - BACKGROUND COLOR - #
  "bg_black"
  "bg_red"
  "bg_green"
  "bg_yellow"
  "bg_blue"
  "bg_magenta"
  "bg_cyan"
  "bg_white"
  "bg_orange"
  "bg_gray"
}
  """
  style = style.split(',')
  for i, itsy in enumerate(style):
    style[i] = itsy.strip()
  
  try:
    if style == ['']:
      raise CodeStyleEmptyError("The style code is empty.")
    else:
      ansi_main = ""
      for key_style in style:
        ansi_main += __ansi_key[key_style]
      return ansi_main + text + '\033[0m'
  except KeyError:
    raise OptionNotFoundError(f"'{', '.join(style)}' The style code is not found.")

# -- func: make a table ascii for terminal | return True -- #
def table(type='table', headers=(['headers']), data=([['data']]), borders=(['\u2500', '\u2502', '\u250c', '\u2510', '\u2514', '\u2518', '\u252c', '\u2534', '\u251c', '\u2524', '\u253c']), rm_ansi=False):
  """
return: True
asciiTUI.table(type=str, headers=list, data=list, borders=list, rm_ansi=bool)

Args:
  type    : Table model type (['table', 'table_fancy-grid', 'tabulate'])
  headers : The header list is in the form of a list type. Example: ['index', 'name'] [<col 1>, <col 2>]
  data    : The data list is in the form of a list type. Example: [['0', 'Michael'], ['1', 'John']] [<row 1>, <row 2>]
  borders : Changing borders (['\u2500', '\u2502', '\u250c', '\u2510', '\u2514', '\u2518', '\u252c', '\u2534', '\u251c', '\u2524', '\u253c'])
  rm_ansi : Removing ansi code when doing len() or .ljust() calculations.
  """
  if isinstance(headers, list) and isinstance(data, list) and isinstance(borders, list):
    pass
  else:
    raise UnboundLocalError("header and data in the form of a list.")
  table_main = ''
  if (type.lower() == 'table') or (type.lower() == 'table_fancy-grid'):
    column_widths = [max(len(remove_ansi(str(item)) if rm_ansi else str(item)) for item in column) for column in zip(headers, *data)]
    header_line =  str(borders[2]) + str(borders[6]).join(str(borders[0]) * (width + 2) for width in column_widths) + str(borders[3])+'\n'
    header = str(borders[1]) + str(borders[1]).join(f" {str(header).center(width)} " for header, width in zip(headers, column_widths)) + str(borders[1])+'\n'
    table_main += header_line
    table_main += header
    for i, row in enumerate(data):
      row_line = str(borders[8]) + str(borders[10]).join(str(borders[0]) * (width + 2) for width in column_widths) + str(borders[9])+'\n'
      row_line_down = str(borders[4]) + str(borders[7]).join(str(borders[0]) * (width + 2) for width in column_widths) + str(borders[5])
      row_content = str(borders[1]) + str(borders[1]).join(f" {str(item) + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width)} " for item, width in zip(row, column_widths)) + str(borders[1])+'\n'
      table_main += (row_line if i == 0 else '') if type.lower() == 'table_fancy-grid' else row_line
      table_main += row_content
    table_main += row_line_down
  elif type.lower() == 'tabulate':
    column_widths = [max(len(remove_ansi(str(header)) if rm_ansi else str(header)), max(len(remove_ansi(str(item)) if rm_ansi else str(item)) for item in col) if col else 0) for header, col in zip(headers, zip(*data))]
    header_str = (' '+str(borders[1])+' ').join([header + ' ' * (width-len(remove_ansi(str(header)))) if rm_ansi else str(header).ljust(width) for header, width in zip(headers, column_widths)])
    table_main += header_str + '\n'
    table_main += str(borders[0]) * len(remove_ansi(header_str) if rm_ansi else header_str) + '\n'
    count = 0
    for row in data:
      row_str = (' '+str(borders[1])+' ').join([item + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width) for item, width in zip(row, column_widths)])
      table_main += row_str + ('\n' if count <= len(data)-2 else '')
      count += 1
  else:
    raise OptionNotFoundError(f"There is no type as '{type}'.")
  return table_main

# -- func: make animation typing text terminal | return False -- #
def typing(text="Hello World! - asciiTUI", speed=0.1):
  """
return: False
asciiTUI.typing(text=str, speed=float)

Args:
  text  : The main text that will be printed with typing animation.
  speed : Set speed.
  """
  for char in text:
    print(char, end='', flush=True)
    time.sleep(speed)
  print()

# -- func: make progress bar ascii terminal | yield True -- #
def progress_bar(type='line', speed=0.1, width=50, max=100, bar_progress="#", bar_space=".", bar_box="[]", text="Hello World! - asciiTUI", isdone=" "):
  """
yield: True
asciiTUI.progress_bar(type=str, speed=float, width=int, clear=bool, max=int, bar_progress=str, bar_space=str, bar_box=str, text=str, isdone=str)

Args:
  type         : Type of progress model ('line' or 'circle').
  speed        : Speed of progress.
  width        : Width length of the progress bar (applies to 'line' type).
  max          : Maximum progress percentage (applies to 'line' type). If it is in the 'circle' type then it is a progress time limit.
  bar_progress : Progress symbol (valid in 'line' type).
  bar_space    : Space bar symbol (valid in 'line' type).
  bar_box      : Progress symbol box (valid in 'line' type).
  text         : Display text in 'circle' type.
  isdone       : Display done in 'circle' type if is done.

Example use:
  import asciiTUI

  pbg = asciiTUI.progress_bar(type='line')
  for i in pbg:
    print(next(pbg), end='\\r')
    asciiTUI.time.sleep(0.01)

Display(s):
  progress_bar('line')
  Output:
  [#########################################] 100.0%

  progress_bar('cicle')
  Output:
  Hello World! - asciiTUI-
  """
  if 'line' in type.lower():
    total = 100
    progress = 0
    bar_start = bar_box[0]
    bar_end = bar_box[-1]
    max = int(max)
    width = int(width)
    speed = float(speed)
    width = width - len(str(max)) - 6
    for i in range(max * 10):
      progress += 1
      percent = total * (progress / float(total) / 10)
      filled_width = int(width * (progress // 10) // max)
      bar = f'{bar_progress}' * filled_width + f'{bar_space}' * (width - filled_width)
      yield f"\r{bar_start}{bar}{bar_end} {percent:.1f}%"
  elif 'circle' in type.lower():
    circle_keys = {0: '-', 1: '\\', 2: '|', 3: '/'}
    count = 0
    while max >= 0:
      yield text + circle_keys[count]
      count += 1
      max -= 1
      if count >= 4:
        count = 0
    yield text + isdone
  else:
    raise OptionNotFoundError(f"'{type.lower()}' The type is not found.")

# -- func: make justify func for text | return True -- #
def justify(content='Hello World! - asciiTUI', make='center', width=50, height=50, space=' ', align=False, rm_ansi=False):
  """
return: True
asciiTUI.justify(content=str, make=str, width=int, space=str, align=bool, rm_ansi=bool)

Args:
  content : Content string to be justified.
  make    : Make the string printed with the center (make='center') or to the right (make='right').
  width   : Set the width size.
  height  : Set the height size.
  space   : Space symbol.
  align   : Makes text center align (depending on size in height).
  rm_ansi : Removing ansi code when doing len() calculations.
  """
  content_lines = content.split('\n')
  content_end = ''
  contents = ''
  content_pieces = []
  for coline in content_lines:
    if rm_ansi:
      if len(remove_ansi(coline)) >= width:
        content_end = str(coline[(len(remove_ansi(coline)) // width) * width:])
        start_index = 0
        while start_index < len(remove_ansi(coline)):
          if start_index + width <= len(remove_ansi(coline)):
            content_pieces.append(coline[start_index:start_index + width])
          start_index += width
      if 'center' in make.lower():
        if len(remove_ansi(coline)) <= width:
          contents += space[0] * ((width - len(remove_ansi(coline))) // 2) + coline + space[0] * ((width - len(remove_ansi(coline))) // 2)
        else:
          for item in content_pieces:
            contents += item + '\n'
          contents += space[0] * ((width - len(remove_ansi(content_end))) // 2) + content_end + space[0] * ((width - len(remove_ansi(content_end))) // 2)
      elif 'right' in make.lower():
        if len(remove_ansi(coline)) <= width:
          contents += space[0] * (width - len(remove_ansi(coline))) + coline
        else:
          for item in content_pieces:
            contents += item + '\n'
          contents += space[0] * (width - len(remove_ansi(content_end))) + content_end
    else:
      content_end = str(coline[(len(coline) // width) * width:])
      start_index = 0
      while start_index < len(coline):
        if start_index + width <= len(coline):
          content_pieces.append(coline[start_index:start_index + width])
        start_index += width
      if 'center' in make.lower():
        if len(coline) <= width:
          contents += space[0] * ((width - len(coline)) // 2) + coline + space[0] * ((width - len(coline)) // 2)
        elif len(coline) >= width:
          for item in content_pieces:
            contents += item + '\n'
          contents += space[0] * ((width - len(content_end)) // 2) + content_end + space[0] * ((width - len(content_end)) // 2)
      elif 'right' in make.lower():
        if len(coline) <= width:
          contents += space[0] * (width - len(coline)) + coline
        elif len(coline) >= width:
          for item in content_pieces:
            contents += item + '\n'
          contents += space[0] * (width - len(content_end)) + content_end
  if align:
    return ("\n" * height) + contents
  else:
    return contents

# -- Special module for Windows -- #
if sys.platform == 'win32':

  # -- func: password input function | return True -- #
  def pwinput(prompt='', mask='*'):
    """
return: True
asciiTUI.pwinput(prompt=str, mask=str)

Args:
  prompt : Appearance of prompt or text.
  mask   : As the character mask displayed.
    """
    STR_TYPE = str
    if not isinstance(prompt, STR_TYPE):
      raise TypeError(f"Prompt argument must be a str, not {type(prompt).__name__}")
    if not isinstance(mask, STR_TYPE):
      raise TypeError(f"Mask argument must be a zero or one character str, not '{type(prompt).__name__}'")
    if len(mask) > 1:
      raise ValueError('Mask argument must be a zero or one character str')
    if mask == '' or sys.stdin is not sys.__stdin__:
      return getpass.getpass(prompt)
    enteredPassword = []
    sys.stdout.write(prompt)
    sys.stdout.flush()
    while True:
      key = ord(getch())
      if key == 13:
        sys.stdout.write('\n')
        return ''.join(enteredPassword)
      elif key in (8, 127):
        if len(enteredPassword) > 0:
          sys.stdout.write('\b \b')
          sys.stdout.flush()
          enteredPassword = enteredPassword[:-1]
      elif 0 <= key <= 31:
        pass
      else:
        char = chr(key)
        sys.stdout.write(mask)
        sys.stdout.flush()
        enteredPassword.append(char)

# -- Special module for MacOS or Linux -- #
else:

  # -- func: replacement for the getch() function in the msvcrt module | return True -- #
  def getch():
    """
return: True
asciiTUI.getch() -> None args or parameters

Info:
  Replacement for the getch() function in the msvcrt module because this library does not support anything other than Windows.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

  # -- func: password input function | return True -- #
  def pwinput(prompt='', mask='*'):
    """
return: True
asciiTUI.pwinput(prompt=str, mask=str)

Args:
  prompt : Appearance of prompt or text.
  mask   : As the character mask displayed.
    """
    STR_TYPE = str
    if not isinstance(prompt, STR_TYPE):
      raise TypeError(f"Prompt argument must be a str, not {type(prompt).__name__}")
    if not isinstance(mask, STR_TYPE):
      raise TypeError(f"Mask argument must be a zero or one character str, not '{type(prompt).__name__}'")
    if len(mask) > 1:
      raise ValueError('Mask argument must be a zero or one character str')
    if mask == '' or sys.stdin is not sys.__stdin__:
      return getpass.getpass(prompt)
    enteredPassword = []
    sys.stdout.write(prompt)
    sys.stdout.flush()
    while True:
      key = ord(getch())
      if key == 13:
        sys.stdout.write('\n')
        return ''.join(enteredPassword)
      elif key in (8, 127):
        if len(enteredPassword) > 0:
          sys.stdout.write('\b \b')
          sys.stdout.flush()
          enteredPassword = enteredPassword[:-1]
      elif 0 <= key <= 31:
        pass
      else:
        char = chr(key)
        sys.stdout.write(mask)
        sys.stdout.flush()
        enteredPassword.append(char)
