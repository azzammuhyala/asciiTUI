"""```
=================== __file__: 'asciiTUI/__init__.py' ===================
======================= import_name : 'asciiTUI' =======================
================= Create By: Azzammuhyala | Indonesian =================
                                                                        
Last Update: 06/01 (January)/2024 <GMT+7>                               
Version    : 1.2.9                                                      
                                                                        
Description: This is a library of tools for you to use with your needs  
               for an attractive type of terminal (console) display.    
                                                                        
Information: Type 'print(dir(asciiTUI))' for further functions, then    
                type 'print(asciiTUI.<func>.__doc__)' for further       
                  document information of each function or full         
                  documentation or full documentation on PyPI :         
                        https://pypi.org/project/asciiTUI               
                                  or on GitHub:                         
                    https://github.com/azzammuhyala/asciiTUI/          
```"""

# -- importing: all: {os, re, sys, getpass, textwrap}, add: {windows: {msvcrt} else: {tty, termios}} -- #
import os as _os
import re as _re
import sys as _sys
import getpass as _getpass
import textwrap as _textwrap
if _sys.platform == 'win32':
  from msvcrt import getch as _getch
else:
  import tty as _tty
  import termios as _termios

# -- var(s) -- #
__version__ = '1.2.9'
module_use  = r'{os, re, sys, getpass, textwrap}, add: {windows: {msvcrt} else: {tty, termios}}'
lorem_ipsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# -- class Error(s) -- #
class OptionNotFoundError(Exception):
  def __init__(self, *message):
    super().__init__(*message)

class PythonVersionError(Exception):
  def __init__(self, *message):
    super().__init__(*message)

# -- Python version checking -- #
if _sys.version_info[0] == 2:
  raise PythonVersionError("asciiTUI only works in python 3, not 2")

# -- func(s) -- #
# -- func: removing ansi code | return [str] -- #
def remove_ansi(text:str) -> str:
  """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> text = '\\033[32mHello World!\\033[36m'
  >>> len(text)
  22
  >>> len(tui.remove_ansi(text=text))
  12

Args:
  `text` : The main text that will remove the ansi code
  """
  text = str(text)
  text = _re.sub(r'\033\[[0-9;]*[mK]', '', text)
  text = _re.sub(r'\x1b\[[0-9;]*[mK]', '', text)
  text = _re.sub(r'\x1B\][0-9;]*[mK]', '', text)
  text = _re.sub(r'\u001b\][0-9;]*[mK]', '', text)
  return text

# -- func: get terminal size | return [int] -- #
def terminal_size(get:str) -> int:
  """
return: `int`

Example use:
  >>> import asciiTUI as tui
  >>> tui.terminal_size(get='x')
  120
  >>> # The numbers above will not match the output results you get. It all depends on the size of your terminal when executed.
  >>> tui.terminal_size(get='xy')
  (120, 30)
  >>> # or
  >>> x, y = tui.terminal_size(get='xy')
  >>> print(x)
  120
  >>> print(y)
  30

Args:
  `get` : The type of terminal size you will get. `x`: width, `y`: height
  """
  get = str(get).lower()
  x, y = _os.get_terminal_size().columns, _os.get_terminal_size().lines
  if get == 'x': return x
  elif get == 'y': return y
  elif get == 'xy': return x, y
  elif get == 'yx': return y, x
  else: raise OptionNotFoundError(f"'{get}' The type (get) is not found.")

# -- func: make color text terminal | return [str] -- #
def rgb(
    r:int=255,
    g:int=255,
    b:int=255,
    style:str='fg'
  ) -> str:
  """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> print("%sHello %sWorld%s!%s" % (tui.rgb(r=0), tui.rgb(r=24,g=90,b=123), tui.rgb(style='bg'), '\\033[0m'))
  Hello World!
  >>> # The resulting output is in the form of RGB colors in general. Style as foreground (fg) or background (bg) type. The resulting color depends on the type of console used.

Args:
  `r`     : Red value (0-255)
  `g`     : Green value (0-255)
  `b`     : Blue value (0-255)
  `style` : Color style, either `fg` for foreground or `bg` for background
  """
  style = str(style).lower()
  if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
    raise TypeError(f"r, g, b is int, and style is str not r:{type(r).__name__}, g:{type(g).__name__}, b:{type(b).__name__}")
  if ((r < 0) or (r > 255)) or ((g < 0) or (g > 255)) or ((b < 0) or (b > 255)):
    raise ValueError(f'The values of r, g, b are not up to standard r:{r}, g:{g}, b:{b}')

  if style == 'fg':
    return f"\u001b[38;2;{r};{g};{b}m"
  elif style == 'bg':
    return f"\u001b[48;2;{r};{g};{b}m"

  else:
    raise OptionNotFoundError(f"'{style}' The type (style) is not found. Only 'fg' (foreground) or 'bg' (background)")

# -- func: make justify func for text | return [str] -- #
def justify(
    content:str,
    width:int,
    make:str='center',
    fill:str=' ',
    height:int=50,
    align:bool=False,
    wrap:bool=True
  ) -> str:
  """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> print(tui.justify(content=tui.lorem_ipsum, width=50, make='center', fill=' ', height=50, align=False, wrap=True))
   Lorem Ipsum is simply dummy text of the printing 
  and typesetting industry. Lorem Ipsum has been the
    industry's standard dummy text ever since the   
   1500s, when an unknown printer took a galley of  
    type and scrambled it to make a type specimen   
  book. It has survived not only five centuries, but
      also the leap into electronic typesetting,    
       remaining essentially unchanged. It was      
     popularised in the 1960s with the release of   
   Letraset sheets containing Lorem Ipsum passages, 
  and more recently with desktop publishing software
   like Aldus PageMaker including versions of Lorem 
                        Ipsum.

Args:
  `content` : Content string to be justified
  `width`   : Set the width size
  `make`    : Make the string printed with the center `center` or to the right `right` or to the left `left`
  `fill`    : Fill character
  `height`  : Set the height size
  `align`   : Makes text center align (depending on size in height)
  `wrap`    : Word wrapping
  """
  content, make, fill = map(str, [content, make, fill])
  fill, make = fill[0], make.lower()
  align, wrap = map(bool, [align, wrap])
  if not (isinstance(width, int) and isinstance(height, int)):
    raise TypeError(f"width, height is int not width:{type(width).__name__}, height:{type(height).__name__}")
  if width < 1:
    return content

  content_lines = content.split('\n')
  content_end = ''
  contents = ''
  content_pieces = []

  def cutting_content(main_text, width):
    content_pieces = []
    content_end = str(main_text[(len(main_text) // width) * width:])
    start_index = 0
    while start_index < len(main_text):
      if start_index + width <= len(main_text):
        content_pieces.append(main_text[start_index:start_index + width])
      start_index += width
    return content_pieces, content_end

  for isline, coline in enumerate(content_lines):
    if len(remove_ansi(coline)) >= width:
      ctn_list, ctn_end = cutting_content(coline, width)
      for item in ctn_list:
        content_pieces.append(item)
      content_end = ctn_end

    if make == 'center':
      if (len(remove_ansi(coline)) <= width) and (not wrap):
        extra_space = width - len(remove_ansi(coline))
        left_padding = extra_space // 2
        right_padding = extra_space - left_padding
        contents += fill * left_padding + coline + fill * right_padding + ('\n' if isline < len(content_lines)-1 else '')
      else:
        if not wrap:
          for item in content_pieces:
            contents += item + '\n'
          extra_space = width - len(remove_ansi(content_end))
          left_padding = extra_space // 2
          right_padding = extra_space - left_padding
          contents += fill * left_padding + content_end + fill * right_padding
        else:
          wraped = _textwrap.wrap(coline, width)
          for i, item_wrap in enumerate(wraped):
            extra_space = width - len(remove_ansi(item_wrap))
            left_padding = extra_space // 2
            right_padding = extra_space - left_padding
            contents += fill * left_padding + item_wrap + fill * right_padding + ('\n' if (i < len(wraped)-1) or (isline < len(content_lines)-1) else '')
      content_pieces.clear()

    elif make == 'right':
      if (len(remove_ansi(coline)) <= width) and (not wrap):
        contents += fill * (width - len(remove_ansi(coline))) + coline + ('\n' if isline < len(content_lines)-1 else '')
      else:
        if not wrap:
          for item in content_pieces:
            contents += item + '\n'
          contents += fill * (width - len(remove_ansi(content_end))) + content_end
        else:
          wraped = _textwrap.wrap(coline, width)
          for i, item_wrap in enumerate(wraped):
            contents += fill * (width - len(remove_ansi(item_wrap))) + item_wrap + ('\n' if (i < len(wraped)-1) or (isline < len(content_lines)-1) else '')
      content_pieces.clear()

    elif make == 'left':
      if (len(remove_ansi(coline)) <= width) and (not wrap):
        contents += coline + fill * (width - len(remove_ansi(coline))) + ('\n' if isline < len(content_lines)-1 else '')
      else:
        if not wrap:
          for item in content_pieces:
            contents += item + '\n'
          contents += content_end + fill * (width - len(remove_ansi(content_end)))
        else:
          wraped = _textwrap.wrap(coline, width)
          for i, item_wrap in enumerate(wraped):
            contents += item_wrap + fill * (width - len(remove_ansi(item_wrap))) + ('\n' if (i < len(wraped)-1) or (isline < len(content_lines)-1) else '')
      content_pieces.clear()

    else:
      raise OptionNotFoundError(f"'{make}' The type (make) is not found.")

  if align:
    return ("\n" * height) + contents
  else:
    return contents

# -- func: make a table ascii for terminal | return [str] -- #
def table(
    headers:list,
    data:list[list],
    typefmt:str='table',
    tjust:list=['center', 'left'],
    borders:list=[
      '\u2500',
      '\u2502',
      '\u250c',
      '\u2510',
      '\u2514',
      '\u2518',
      '\u252c',
      '\u2534',
      '\u251c',
      '\u2524',
      '\u253c'
    ]
  ) -> str:
  """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> print(tui.table(
  ...   headers = ['NUM', 'Name'],
  ...   data    = [
  ...               [1, 'Alice'],
  ...               [2, 'Steve'],
  ...             ],
  ...   typefmt = 'table',
  ...   tjust   = ['center', 'left'],
  ...   borders = ['\\u2500', '\\u2502', '\\u250c', '\\u2510', '\\u2514', '\\u2518', '\\u252c', '\\u2534', '\\u251c', '\\u2524', '\\u253c'] # need 11 borders
  ... ))
  ┌─────┬───────┐
  │ NUM │ Name  │
  ├─────┼───────┤
  │ 1   │ Alice │
  ├─────┼───────┤
  │ 2   │ Steve │
  └─────┴───────┘

Model types:
  >>> # 'table' Types of table models in general.
  ┌─────┬───────┐
  │ NUM │ Name  │
  ├─────┼───────┤
  │ 1   │ Alice │
  ├─────┼───────┤
  │ 2   │ Steve │
  └─────┴───────┘
  >>> # 'table_fancy-grid' Table model type without rows in the data.
  ┌─────┬───────┐
  │ NUM │ Name  │
  ├─────┼───────┤
  │ 1   │ Alice │
  │ 2   │ Steve │
  └─────┴───────┘
  >>> # 'tabulate' Tabulate model type with minimal borders.
  NUM │ Name 
  ───────────
  1   │ Alice
  2   │ Steve

Args:
  `headers` : The header list is in the form of a list type. Example: `['NUM', 'Name'] [<col 1>, <col 2>]`
  `data`    : The data list is in the form of a list type. Example: `[[1, 'Alice'], [2, 'Steve']] [<row 1>, <row 2>]`
  `typefmt` : Table model type (`table` or `table_fancy-grid` or `tabulate`)
  `tjust`   : Justify the layout of headers and data (`center` or `right` or `left`). (using `justify()` function). Index: `[<make:headers>, <make:data>]`
  `borders` : Changing borders, default: (`['\\u2500', '\\u2502', '\\u250c', '\\u2510', '\\u2514', '\\u2518', '\\u252c', '\\u2534', '\\u251c', '\\u2524', '\\u253c']`)
  """
  if not (isinstance(headers, list) and isinstance(data, list) and isinstance(tjust, list) and isinstance(borders, list)):
    raise TypeError(f"headers, data, borders type is list not headers:{type(headers).__name__}, data:{type(data).__name__}, borders:{type(borders).__name__}")
  for item in data:
    if not isinstance(item, list): raise TypeError(f"data type in it must be a list not {type(item).__name__}")
  if len(tjust) != 2:
    raise ValueError(f"tjust length cannot be less or more than 2 not {len(tjust)}")
  if len(borders) != 11:
    raise ValueError(f'borders length cannot be less or more than 11 not {len(borders)}')

  typefmt = str(typefmt).lower()
  headers = [str(item) for item in headers]
  data = [[str(item) for item in row] for row in data]
  tjust = [str(item) for item in tjust]
  borders = [str(item)[0] for item in borders]
  table_main = ''

  if (typefmt == 'table') or (typefmt == 'table_fancy-grid'):
    column_widths = [max(len(remove_ansi(item)) for item in column) for column in zip(headers, *data)]
    header_line =  borders[2] + borders[6].join(borders[0] * (width + 2) for width in column_widths) + borders[3]+'\n'
    header = borders[1] + borders[1].join(f" {justify(header, width, tjust[0], wrap=False)} " for header, width in zip(headers, column_widths)) + borders[1]+'\n'
    table_main += header_line
    table_main += header
    for i, row in enumerate(data):
      row_line = borders[8] + borders[10].join(borders[0] * (width + 2) for width in column_widths) + borders[9]+'\n'
      row_line_down = borders[4] + borders[7].join(borders[0] * (width + 2) for width in column_widths) + borders[5]
      row_content = borders[1] + borders[1].join(f" {justify(item, width, tjust[1], wrap=False)} " for item, width in zip(row, column_widths)) + borders[1]+'\n'
      table_main += (row_line if i == 0 else '') if typefmt == 'table_fancy-grid' else row_line
      table_main += row_content
    table_main += row_line_down

  elif typefmt == 'tabulate':
    column_widths = [max(len(remove_ansi(header)), max(len(remove_ansi(item)) for item in col) if col else 0) for header, col in zip(headers, zip(*data))]
    header_str = f' {borders[1]} '.join([justify(header, width, tjust[0], wrap=False) for header, width in zip(headers, column_widths)])
    table_main += header_str + '\n'
    table_main += borders[0] * len(remove_ansi(header_str)) + '\n'
    count = 0
    for row in data:
      row_str = f' {borders[1]} '.join([justify(item, width, tjust[1], wrap=False) for item, width in zip(row, column_widths)])
      table_main += row_str + ('\n' if count <= len(data)-2 else '')
      count += 1

  else:
    raise OptionNotFoundError(f"'{typefmt}' The type (typefmt) is not found.")

  return table_main

# -- class -- #
# -- func class: splits multiple command arguments on a string | return [None, list, list[list]] -- #
class Init_cmd_split:

  def __init__(self,
                esc_char:str='\\',
                quotes_char:str='"',
                ln_char:str=';',
                backslash_char:str='\\',
                param_char:str=' '
              ) -> None:
    """
Functions (method): `split_args`, `split_ln`
return: `None`

Example use:
  >>> import asciiTUI as tui
  >>> cs = tui.Init_cmd_split(esc_char='\\\\', quotes_char='"', ln_char=';', backslash_char='\\\\', param_char=' ')
  >>> # Other method documentation is in each method..

Args:
  `esc_char`       : Escape character
  `quotes_char`    : Quote character
  `ln_char`        : Line character. To separate and create rows
  `backslash_char` : Backslash character
  `param_char`     : Parameter character. To separate parameters
    """
    self.esc_char, self.quotes_char, self.ln_char, self.backslash_char, self.param_char = map(str, [esc_char, quotes_char, ln_char, backslash_char, param_char])
    if (len(self.esc_char) != 1) or (len(self.quotes_char) != 1) or (len(self.ln_char) != 1) or (len(self.backslash_char) != 1) or (len(self.param_char) != 1):
      raise ValueError("All characters only consist of 1 character")

  def split_args(self, cmd:str) -> list[list]:
    """
return: `list[list]`

Example use:
  >>> command = r'pip install asciiTUI; echo "Hello World!\\""; py'
  >>> cs.split_args(cmd=command)
  [['pip', 'install', 'asciiTUI'], ['echo', 'Hello World!"'], ['py']]

Args:
  `cmd` : main command string
    """
    cmd = str(cmd)
    result = []
    in_quotes = False
    current_cmd = ''
    params = []
    escape_char = False

    for char in cmd:
      if char == self.esc_char and not escape_char:
        escape_char = True
      elif char == self.quotes_char and not escape_char:
        in_quotes = not in_quotes
      elif char == self.ln_char and not in_quotes:
        if current_cmd or params:
          result.append(params + [current_cmd])
          current_cmd = ''
          params = []
      elif char == self.param_char and not in_quotes:
        if current_cmd:
          params.append(current_cmd)
          current_cmd = ''
      else:
        if escape_char and char == self.backslash_char:
          current_cmd += char
          escape_char = False
        else:
          current_cmd += char
          escape_char = False

    if current_cmd or params:
      result.append(params + [current_cmd])

    return result

  def split_ln(self, cmd:str) -> list:
    """
return: `list`

Example use:
  >>> command = r'pip install asciiTUI; echo "Hello World!\\""; py'
  >>> cs.split_ln(cmd=command)
  ['pip install asciiTUI', 'echo "Hello World!\\\\""', 'py']

Args:
  `cmd` : main command string
    """
    cmd = str(cmd)
    result = []
    in_quotes = False
    current_cmd = ''
    escape_char = False

    for char in cmd:
      if char == self.esc_char and not escape_char:
        escape_char = True
      elif char == self.quotes_char and not escape_char:
        in_quotes = not in_quotes
        current_cmd += char
      elif char == self.ln_char and not in_quotes:
        if current_cmd:
          result.append(current_cmd.strip())
          current_cmd = ''
      else:
        if char == self.quotes_char and escape_char:
          current_cmd += self.esc_char
        current_cmd += char
        escape_char = False

    if current_cmd:
      result.append(current_cmd.strip())

    return result

# -- func class: make progress bar ascii terminal | return [None, str] -- #
class Init_progress_bar:
  def __init__(self,
                typefmt:str='simple-box',
                width:int=50,
                maxp:int=100,
                showpercent:bool=True,
                bar_borders:list=[
                  "#",
                  ".",
                  "[",
                  "]"
                ]
              ) -> None:
    """
Functions (method): `strbar`
return: `None`

Example use:
  >>> import asciiTUI as tui
  >>> pb = tui.Init_progress_bar(typefmt='simple-box', width=50, maxp=100, showpercent=True, bar_borders=["#", ".", "[", "]"])
  >>> # Other method documentation is in each method..

Args:
  `typefmt`     : The model type (`simple-box` or `simple line`)
  `width`       : Set width size
  `maxp`        : Set max percent and progress
  `showpercent` : Displays the percent figure on progress
  `bar_borders` : Borders bar
    """
    if not (isinstance(width, int) and isinstance(maxp, int) and isinstance(bar_borders, list)):
      raise TypeError(f"width, maxp is int not width:{type(width).__name__}, maxp:{type(maxp).__name__}")
    if len(bar_borders) != 4:
      raise ValueError(f'bar_borders length cannot be less or more than 4 not {len(bar_borders)}')
    self.showpercent = bool(showpercent)
    self.typefmt = str(typefmt).lower()
    self.maxp, self.width = map(int, [maxp, width])
    self.bar_borders = [str(item) for item in bar_borders]

  def strbar(self, progress:int|float) -> str:
    """
return: `str`

Example use:
  >>> print(pb.strbar(progress=12.4)) # 12.4%
  [#####....................................] 12.4%

Model types:
  >>> # 'simple-box' Simple progress box model
  [#########################################] 100.0%
  >>> # 'simple-line' Simple progress line model
  ########################################### 100.0%

Args:
  `progress` : Current percent progress
    """
    if not (isinstance(progress, int) or isinstance(progress, float)):
      raise TypeError(f"progress is (int or float) not progress:{type(progress).__name__}")
    if self.width < len(str(self.maxp)) + 7:
      return f"{progress:.1f}%"

    bar = lambda w: self.bar_borders[0] * int(w * progress // self.maxp) + self.bar_borders[1] * (w - int(w * progress // self.maxp))

    if self.typefmt == 'simple-box':
      w = self.width - len(str(self.maxp)) - 6 if self.showpercent else self.width - 2
      return f"{self.bar_borders[2]}{bar(w)}{self.bar_borders[3]} {progress:.1f}%" if self.showpercent else self.bar_borders[2]+bar(w)+self.bar_borders[3]

    elif self.typefmt == 'simple-line':
      w = self.width - len(str(self.maxp)) - 4 if self.showpercent else self.width
      return f"{bar(w)} {progress:.1f}%" if self.showpercent else bar(w)

    else:
      raise OptionNotFoundError(f"'{self.typefmt}' The type is not found.")

# -- Special module for Windows -- #
if _sys.platform == 'win32':

  # -- func: password input function | return [str] -- #
  def pwinput(prompt:str='', mask:str='*') -> str:
    """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> password = tui.pwinput(prompt='Password: ', mask='*'); print(password)
  Password: ***********
  Hello World

Args:
  `prompt` : Appearance of prompt or text.
  `mask`   : As the character mask displayed.
    """
    prompt, mask = map(str, [prompt, mask])
    if len(mask) > 1:
      raise ValueError('Mask argument must be a zero or one character str')
    if mask == '' or _sys.stdin is not _sys.__stdin__:
      return _getpass.getpass(prompt)
    enteredPassword = []
    _sys.stdout.write(prompt)
    _sys.stdout.flush()
    while True:
      key = ord(_getch())
      if key == 13:
        _sys.stdout.write('\n')
        return ''.join(enteredPassword)
      elif key in (8, 127):
        if len(enteredPassword) > 0:
          _sys.stdout.write('\b \b')
          _sys.stdout.flush()
          enteredPassword = enteredPassword[:-1]
      elif 0 <= key <= 31:
        pass
      else:
        char = chr(key)
        _sys.stdout.write(mask)
        _sys.stdout.flush()
        enteredPassword.append(char)

# -- Special module for MacOS or Linux -- #
else:

  # -- func: replacement for the getch() function in the msvcrt module | return [str] -- #
  def getch() -> str:
    """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> tui.getch() # none args or parameters
  'S'

Info:
  Replacement for the `getch()` function in the msvcrt module because this library does not support anything other than Windows.
    """
    fd = _sys.stdin.fileno()
    old_settings = _termios.tcgetattr(fd)
    try:
      _tty.setraw(_sys.stdin.fileno())
      ch = _sys.stdin.read(1)
    finally:
      _termios.tcsetattr(fd, _termios.TCSADRAIN, old_settings)
    return ch

  # -- func: password input function | return [str] -- #
  def pwinput(prompt:str='', mask:str='*') -> str:
    """
return: `str`

Example use:
  >>> import asciiTUI as tui
  >>> password = tui.pwinput(prompt='Password: ', mask='*'); print(password)
  Password: ***********
  Hello World

Args:
  `prompt` : Appearance of prompt or text.
  `mask`   : As the character mask displayed.
    """
    prompt, mask = map(str, [prompt, mask])
    if len(mask) > 1:
      raise ValueError('Mask argument must be a zero or one character str')
    if mask == '' or _sys.stdin is not _sys.__stdin__:
      return _getpass.getpass(prompt)
    enteredPassword = []
    _sys.stdout.write(prompt)
    _sys.stdout.flush()
    while True:
      key = ord(getch())
      if key == 13:
        _sys.stdout.write('\n')
        return ''.join(enteredPassword)
      elif key in (8, 127):
        if len(enteredPassword) > 0:
          _sys.stdout.write('\b \b')
          _sys.stdout.flush()
          enteredPassword = enteredPassword[:-1]
      elif 0 <= key <= 31:
        pass
      else:
        char = chr(key)
        _sys.stdout.write(mask)
        _sys.stdout.flush()
        enteredPassword.append(char)

# test functions
if __name__ == '__main__':
  pass
