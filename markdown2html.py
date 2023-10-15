#!/usr/bin/python3

"""
Markdown script using python.
"""
import sys
import os.path
import re

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    
    # save file
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print("Missing {}".format(input_file), file=sys.stderr)
        exit(1)

    # read .md content
    with open(input_file, 'r') as md_file:
        md_content = md_file.readlines()

    # keep track of the html content
    html_content = []

    # convert md to html
    for line in md_content:
        if line.strip() != "":
            match = re.compile(r'^(#{1,6})\s(.+)$', re.MULTILINE).match(line)
            level = len(match.group(1))
            text = match.group(2)
            html_content.append(f'<h{level}>{text}</h{level}>')

    # write in output file
    with open(output_file, 'w') as html_file:
        for line in html_content:
            html_file.write(f'{line}\n')

    exit(0)
