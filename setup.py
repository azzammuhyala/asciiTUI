from distutils.core import setup

with open('README.md', 'r', encoding='utf8') as README:
    README_md = README.read()

setup(
    name         = 'asciiTUI',
    version      = '1.2.8',
    author       = 'azzammuhyala',
    author_email = 'azzammuhyala@gmail.com',
    description  = 'This is a library of tools for you to use with your needs for an attractive type of terminal (console) display.',
    url          = 'https://github.com/azzammuhyala/asciiTUI',
    keywords     = ['asciiTUI', 'asciitui', 'ascii', 'tui', 'console', 'text-based', 'tools', 'attractive', 'terminal', 'basic-tools', 'text', 'art-ascii', 'remove_ansi', 'ansi', 'terminal_size', 'rgb', 'table', 'tabulate', 'progress_bar', 'justify', 'justifytext', 'justify-text', 'command_split', 'cmd_split', 'pwinput', 'basic', 'console-display'],
    packages     = ['asciiTUI'],
    long_description_content_type ='text/markdown',
    long_description              = README_md
)
