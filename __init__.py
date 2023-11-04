"""
======================= file_name: '__init__.py' =======================
======================= import_name : 'asciiTUI' =======================

Last Update: 04/11/2023 (GMT+7)
Description: This is a library of tools for you to use with your needs
               for an attractive type of terminal (console) display.
"""

# -- importing: time, os, sys -- #
import time, os, sys

# -- var(s) -- #
module_use   = 'time, os, sys'
__version__  = '1.0.0'
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

# -- class Error(s) -- #
class CodeStyleEmptyError(Exception):
  def __init__(self):
    super().__init__("The style code is empty.")

class CodeStyleNotFoundError(Exception):
  def __init__(self, style):
    super().__init__(f"'{style}' The style code is not found.")

class TypeSizeGet(Exception):
  def __init__(self, args):
    super().__init__(f"There is no type as '{args}'.")

class Python2VersionError(Exception):
  def __init__(self):
    super().__init__("asciiTUI only works in python 3, not 2")

# -- Python version checking -- #
if sys.version_info[0] == 2:
  raise Python2VersionError

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
    text = text.replace(code, "")
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
    raise TypeSizeGet(get)

# -- func: make color text terminal | return True -- #
def colored(text="colored(<Your text>, <color or style>, <add style1>, <add style2>)", style="white"):
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
      raise CodeStyleEmptyError()
    else:
      ansi_main = ""
      for key_style in style:
        ansi_main += __ansi_key[key_style]
      return ansi_main + text + '\033[0m'
  except KeyError:
    raise CodeStyleNotFoundError(', '.join(style))

# -- func: make a table ascii for terminal | return True -- #
def table(type='table', headers=(['headers']), data=([['data']]), using_unicode=False, rm_ansi=False):
  """
return: True
asciiTUI.table(type=str, headers=list, data=list, using_unicode=bool, rm_ansi=bool)

Args:
  type          : Table model type ('table' or 'tabulate')
  headers       : The header list is in the form of a list type. Example: ['index', 'name'] [<col 1>, <col 2>]
  data          : The data list is in the form of a list type. Example: [['0', 'Michael'], ['1', 'John']] [<row 1>, <row 2>]
  using_unicode : Performing a return using a unicode table.
  rm_ansi       : Removing ansi code when doing len() or .ljust() calculations.
  """
  table_main = ''
  if type.lower() == 'table':
    column_widths = [max(len(remove_ansi(str(item)) if rm_ansi else str(item)) for item in column) for column in zip(headers, *data)]
    header_line =  "\u250c" + "\u252c".join("\u2500" * (width + 2) for width in column_widths) + "\u2510\n" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+\n"
    header = "\u2502" + "\u2502".join(f" {header.center(width)} " for header, width in zip(headers, column_widths)) + "\u2502\n" if using_unicode else "|" + "|".join(f" {header.center(width)} " for header, width in zip(headers, column_widths)) + "|\n"
    table_main += header_line
    table_main += header
    for row in data:
      row_line = "\u251c" + "\u253c".join("\u2500" * (width + 2) for width in column_widths) + "\u2524\n" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+\n"
      row_line_down = "\u2514" + "\u2534".join("\u2500" * (width + 2) for width in column_widths) + "\u2518" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
      row_content = "\u2502" + "\u2502".join(f" {str(item) + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width)} " for item, width in zip(row, column_widths)) + "\u2502\n" if using_unicode else "|" + "|".join(f" {str(item) + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width)} " for item, width in zip(row, column_widths)) + "|\n"
      table_main += row_line
      table_main += row_content
    table_main += row_line_down
  elif type.lower() == 'tabulate':
    column_widths = [max(len(remove_ansi(str(header)) if rm_ansi else str(header)), max(len(remove_ansi(str(item)) if rm_ansi else str(item)) for item in col) if col else 0) for header, col in zip(headers, zip(*data))]
    header_str = " \u2502 ".join([header + ' ' * (width-len(remove_ansi(str(header)))) if rm_ansi else header.ljust(width) for header, width in zip(headers, column_widths)]) if using_unicode else " | ".join([header + ' ' * (width-len(remove_ansi(str(header)))) if rm_ansi else header.ljust(width) for header, width in zip(headers, column_widths)])
    table_main += header_str + '\n'
    table_main += "\u2500" * len(remove_ansi(header_str) if rm_ansi else header_str) + '\n' if using_unicode else "-" * len(remove_ansi(header_str) if rm_ansi else header_str) + '\n'
    count = 0
    for row in data:
      row_str = " \u2502 ".join([item + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width) for item, width in zip(row, column_widths)]) if using_unicode else " | ".join([item + ' ' * (width-len(remove_ansi(str(item)))) if rm_ansi else str(item).ljust(width) for item, width in zip(row, column_widths)])
      table_main += row_str + ('\n' if count <= len(data)-2 else '')
      count += 1
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

# -- func: make progress bar ascii terminal | return False -- #
def progress_bar(type='line', speed=0.1, width=50, clear=True, max=100, bar_progress="#", bar_space=".", bar_box="[]", text="Hello World! - asciiTUI", isdone=" "):
  """
return: False
asciiTUI.progress_bar(type=str, speed=float, width=int, clear=bool, max=int, bar_progress=str, bar_space=str, bar_box=str, text=str, isdone=str)

Args:
  type         : Type of progress model ('line' or 'circle').
  speed        : Speed of progress.
  width        : Width length of the progress bar (applies to 'line' type).
  clear        : Select whether to delete bar content or not.
  max          : Maximum progress percentage (applies to 'line' type). If it is in the 'circle' type then it is a progress time limit.
  bar_progress : Progress symbol (valid in 'line' type).
  bar_space    : Space bar symbol (valid in 'line' type).
  bar_box      : Progress symbol box (valid in 'line' type).
  text         : Display text in 'circle' type.
  isdone       : Display done in 'circle' type if is done.

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
    bar_start = bar_box[:1]
    bar_end = bar_box[1:]
    max = int(max)
    width = int(width)
    speed = float(speed)
    width = width - len(str(max)) - 6
    for i in range(max * 10):
      progress += 1
      percent = total * (progress / float(total) / 10)
      filled_width = int(width * (progress // 10) // max)
      bar = f'{bar_progress}' * filled_width + f'{bar_space}' * (width - filled_width)
      print(f"\r{bar_start}{bar}{bar_end} {percent:.1f}%", end="\r") if clear else print(f"{bar_start}{bar}{bar_end} {percent:.1f}%")
      time.sleep(speed / 10)
  elif 'circle' in type.lower():
    circle_keys = {0: '-', 1:'\\', 2: '|', 3: '/'}
    count = 0
    while max >= 0:
      print(text + circle_keys[count], end='\r') if clear else print(text + circle_keys[count])
      count += 1
      max -= 1
      time.sleep(speed / 10)
      if count >= 4:
        count = 0
    print(text + isdone)

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
  content_pieces = []
  content_end = ''
  contents = ''
  if rm_ansi:
    if len(remove_ansi(content)) >= width:
      content_end = str(content[(len(remove_ansi(content)) // width) * width:])
      start_index = 0
      while start_index < len(remove_ansi(content)):
        if start_index + width <= len(remove_ansi(content)):
          content_pieces.append(content[start_index:start_index + width])
        start_index += width
    if 'center' in make.lower():
      if len(remove_ansi(content)) <= width:
        contents += space[:1] * ((width - len(remove_ansi(content))) // 2) + content + space[:1] * ((width - len(remove_ansi(content))) // 2)
      else:
        for item in content_pieces:
          contents += item + '\n'
        contents += space[:1] * ((width - len(remove_ansi(content_end))) // 2) + content_end + space[:1] * ((width - len(remove_ansi(content_end))) // 2)
    elif 'right' in make.lower():
      if len(remove_ansi(content)) <= width:
        contents += space[:1] * (width - len(remove_ansi(content))) + content
      else:
        for item in content_pieces:
          contents += item + '\n'
        contents += space[:1] * (width - len(remove_ansi(content_end))) + content_end
    if align:
      return ("\n" * height) + contents
    else:
      return contents
  else:
    content_end = str(content[(len(content) // width) * width:])
    start_index = 0
    while start_index < len(content):
      if start_index + width <= len(content):
        content_pieces.append(content[start_index:start_index + width])
      start_index += width
    if 'center' in make.lower():
      if len(content) <= width:
        contents += space[:1] * ((width - len(content)) // 2) + content + space[:1] * ((width - len(content)) // 2)
      elif len(content) >= width:
        for item in content_pieces:
          contents += item + '\n'
        contents += space[:1] * ((width - len(content_end)) // 2) + content_end + space[:1] * ((width - len(content_end)) // 2)
    elif 'right' in make.lower():
      if len(content) <= width:
        contents += space[:1] * (width - len(content)) + content
      elif len(content) >= width:
        for item in content_pieces:
          contents += item + '\n'
        contents += space[:1] * (width - len(content_end)) + content_end
    if align:
      return ("\n" * height) + contents
    else:
      return contents