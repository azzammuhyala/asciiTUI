Python asciiTUI
===============

Description
-----------
This is a library of tools for you to use with your needs for an attractive type of terminal (console) display.
Type `print(dir(asciiTUI))` for further functions, then type `print(asciiTUI.<func>.__doc__)` for further document information of each function.

Installation
------------
To install the Python libraries and command line utilities, run:
```shell
pip install asciiTUI
```
If you want to upgrade this library do the command:
```shell
pip install asciiTUI --upgrade
```
or
```shell
pip install asciiTUI==<version>
```
When the installation is complete, import the `asciiTUI` module
```pycon
>>> import asciiTUI as tui
```

Libary usage - Variable
=======================

lorem_ipsum
-----------
This is a `lorem_ipsum` variable which contains the lorem ipsum text in English form. With the following usage:
```pycon
>>> print(tui.lorem_ipsum)
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
```

Libary usage - Functions and Class
==================================

remove_ansi
-----------
The `remove_ansi()` function is used to remove or clean existing ansi escape codes \\033, \\x1b, and others and return the cleaned text. As usage:
```pycon
>>> text = '\033[32mHello World!\033[36m'
>>> len(text) # check length
22
>>> len(tui.remove_ansi(text=text)) # check length and removing ansi escape
12
```
Args:
-   `text` (required) (type: str[auto]) : The main text that will remove the ansi code

terminal_size
-------------
The `terminal_size()` function is used to get the terminal size `x`:width or `y`:height. As usage:
```pycon
>>> tui.terminal_size(get='x')
120
>>> # The numbers above will not match the output results you get. It all depends on the size of your terminal when executed.
>>> tui.terminal_size(get='xy')
(120, 30)
```
You can directly get x and y in one function with `get='xy'` or `get='yx'` as usage:
```pycon
>>> x, y = tui.terminal_size(get='xy')
>>> print(x)
120
>>> print(y)
30
```
Args:
-   `get` (required) (type: str[auto]) : The type of terminal size you will get. `x`: width, `y`: height

Raises:
-   `OptionNotFoundError` : If the `get` option is not found for example searching for anything other than `x` and `y` the results will throw this exception

rgb
---
The `rgb()` function is used to display colored text with the number of colors depending on the code `r, g, b` entered and can display `style` format in the form of `fg` (foreground) or `bg` (background). As usage:
```pycon
>>> print(tui.rgb(r=23, g=102, b=7, style='fg')+'Hello World!'+tui.rgb())
Hello World!
>>> # The resulting output is in the form of RGB colors in general. Style as foreground (fg) or background (bg) type. The resulting color depends on the type of console used.
```
Args:
-   `r` (default: 255) (type: int[None]) : Red value (0-255)
-   `g` (default: 255) (type: int[None]) : Green value (0-255)
-   `b` (default: 255) (type: int[None]) : Blue value (0-255)
-   `style` (default: 'fg') (type: str[auto]) : Color style, either `fg` for foreground or `bg` for background

Raises:
-   `TypeError` : If type `r, g, b` is not `int`
-   `ValueError` : If `r, g, b` is one of the values less than 0 and more than 255
-   `OptionNotFoundError` : If `style` option is not found

justify
-------
The `justify()` function is used to load string text to be in the middle or on the left and can adjust the width size to suit the terminal size or not according to needs. As usage:
```pycon
>>> print(tui.justify(
...   content=tui.lorem_ipsum,
...   width=50,
...   make='center',
...   fill=' ',
...   height=50,
...   align=False,
...   wrap=True
... ))
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
```
There are types of `make` that can be printed, namely:
```shell
make='center'
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

make='right'
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

make='left'
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
```
Args:
-   `content` (required) (type: str[auto]) : Content string to be justified
-   `width` (required) (type: int[None]) : Set the width size
-   `make` (default: 'center') (type: str[auto]) : Make the string printed with the center `center` or to the right `right` or to the left `left`
-   `fill` (default: ' ') (type: str[auto]) : Fill character
-   `height` (default: 50) (type: int[None]) : Set the height size
-   `align` (default: False) (type: bool[auto]) : Makes text center align (depending on size in height)
-   `wrap` (default: True) (type: bool[auto]) : Word wrapping

Raises:
-   `TypeError` : If `width, height` are not `int`
-   `OptionNotFoundError` : If `typefmt` option is not found

table
-----
The `table()` function is used to create an art ASCII table with headers and data in list form. As usage:
```pycon
>>> print(tui.table(
...   headers = ['NUM', 'Name'],
...   data    = [
...               [1, 'Alice'],
...               [2, 'Steve'],
...             ],
...   typefmt = 'table',
...   tjust   = ['center', 'left'],
...   borders = ['\u2500', '\u2502', '\u250c', '\u2510', '\u2514', '\u2518', '\u252c', '\u2534', '\u251c', '\u2524', '\u253c'] # need 11 borders
... ))
┌─────┬───────┐
│ NUM │ Name  │
├─────┼───────┤
│ 1   │ Alice │
├─────┼───────┤
│ 2   │ Steve │
└─────┴───────┘
```
If you experience problems with the console displaying borders, you can change the borders as follows:
`borders=['-', '|', '+', '+', '+', '+', '+', '+', '+', '+', '+']`
Output:
```shell
+-----+-------+
| NUM | Name  |
+-----+-------+
| 1   | Alice |
+-----+-------+
| 2   | Steve |
+-----+-------+
```
There are 3 types of table displays, namely `table`, `table_fancy-grid`, `tabulate`, here are some displays of each type:
```shell
typefmt='table'
┌─────┬───────┐
│ NUM │ Name  │
├─────┼───────┤
│ 1   │ Alice │
├─────┼───────┤
│ 2   │ Steve │
└─────┴───────┘

typefmt='table_fancy-grid'
┌─────┬───────┐
│ NUM │ Name  │
├─────┼───────┤
│ 1   │ Alice │
│ 2   │ Steve │
└─────┴───────┘

typefmt='tabulate'
NUM │ Name 
───────────
1   │ Alice
2   │ Steve
```
Args:
-   `headers` (required) (type: list[None]) : The header list is in the form of a list type. Example: `['NUM', 'Name'] [<col 1>, <col 2>]`
-   `data` (requared) (type: (list[None] values> list[None]) ) : The data list is in the form of a list type. Example: `[[1, 'Alice'], [2, 'Steve']] [<row 1>, <row 2>]`
-   `typefmt` (default: 'table') (type: str[auto]) : Table model type (`table` or `table_fancy-grid` or `tabulate`)
-   `tjust` (default: ['center', 'left']) (type: list[None]) : Justify the layout of headers and data (`center` or `right` or `left`). (using `justify()` function). Index: `[<make:headers>, <make:data>]`
-   `borders` (default: ['\\u2500', '\\u2502', '\\u250c', '\\u2510', '\\u2514', '\\u2518', '\\u252c', '\\u2534', '\\u251c', '\\u2524', '\\u253c']) (type: list[None]) : Changing borders

Raises:
-   `TypeError` : If the `header, data, tjust, borders` type is not a list
-   `ValueError` : If the contents of the `borders, tjust` list are less or more than borders:11, tjust:2
-   `OptionNotFoundError` : If `typefmt` option is not found

Init_cmd_split
--------------
The `Init_cmd_split()` class is an init character used to split command line arguments separated by delimiters defined in this class, such as escape characters, quotes, line breaks, and other special characters. As usage:
```pycon
>>> cs = tui.Init_cmd_split(
...   esc_char='\\',
...   quotes_char='"',
...   ln_char=';',
...   backslash_char='\\',
...   param_char=' '
... )
>>> command = r'pip install asciiTUI; echo "Hello World!\""; py' # main command
```
Args:
-   `esc_char` (default: '\\\\') (type: str[auto]) : Escape character
-   `quotes_char` (default: '"') (type: str[auto]) : Quote character
-   `ln_char` (default: ';') (type: str[auto]) : Line character. To separate and create rows
-   `backslash_char` (default: '\\\\') (type: str[auto]) : Backslash character
-   `param_char` (default: ' ') (type: str[auto]) : Parameter character. To separate parameters

Functions (method):

split_args
----------
This method will separate arguments and lines in list form as usage:
```pycon
>>> cs.split_args(cmd=command)
[['pip', 'install', 'asciiTUI'], ['echo', 'Hello World!"'], ['py']]
```
Args:
-   `cmd` (required) (type: str[auto]) : Main command string

split_ln
--------
This method will separate only rows in list form as usage:
```pycon
>>> cs.split_ln(cmd=command)
['pip install asciiTUI', 'echo "Hello World!\""', 'py']
```
Args:
-   `cmd` (required) (type: str[auto]) : Main command string

Raises:
-   `Init_cmd_split`: `ValueError` : If all arguments or parameters are less or more than 1 in length

Init_progress_bar
-----------------
The `Init_progress_bar()` class is used to load a loading or progress display on the console. As usage:
```pycon
>>> from time import sleep
>>> pb = tui.Init_progress_bar(
...   typefmt='simple-box',
...   width=50,
...   maxp=100,
...   showpercent=True,
...   bar_borders=["#", ".", "[", "]"]
... )
```
Here are some types of progress bars:
```shell
typefmt='simple-box'
[#########################################] 100.0%

typefmt='simple-line', bar_borders=['=', '-', '[', ']']
=========================================== 100.0%
```
Args:
-   `typefmt` (default: 'simple-box') (type: str[auto]) : Type of progress model (`simple-box` or `simple-line`)
-   `width` (default: 50) (type: int[None]) : Width length of the progress bar
-   `maxp` (default: 100) (type: int[None]) : Maximum progress percentage
-   `showpercent` (default : True) (type: bool[auto]): Displays progress percent
-   `bar_borders` (default : ["#", ".", "[", "]"]) (type: list[None]) : Changing borders

Functions (method):

strbar
------
This method is a method for producing a progress bar output with specified progress. As usage:
```pycon
>>> print(pb.strbar(progress=12.4)) # 12.4%
[#####....................................] 12.4%
```
Args:
-   `progress` (required) (type: int[None]) : Current percent progress

Raises:
-   `Init_progress_bar`: `TypeError` : If `width, maxp` are not `int`
-   `Init_progress_bar`: `ValueError` : If the contents of the `bar_borders` list are less or more than 4
-   `strbar`: `TypeError` : If the `progress` type is not `int` or `float`
-   `strbar`: `OptionNotFoundError` : If `typefmt` option is not found

pwinput
-------
The `pwinput()` function is used to take input from the user, but the typed display is only a mask so that the input entered cannot be read. As usage:
```pycon
>>> pw = tui.pwinput(prompt='Password: ', mask='*'); print(pw)
Password: ***********
Hello World
```
Args:
-   `prompt` (default: '') (type: str[auto]) : Appearance of prompt or text.
-   `mask` (default: '*') (type: str[auto]) : As the character mask displayed.

Raises:
-   `ValueError` : If the `mask` length is more than 1 character

Errors
======

OptionNotFoundError
-------------------
If an option or type entered is not found

PythonVersionError
------------------
If you are using Python version 2

CHANGE LOG
==========

1.2.9
-----
-   Fix justify function
-   Fix Init_cmd_split
-   Documentation updates
