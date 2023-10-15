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
    # keep track of list_item
    list_item = ['<ul>']

    # convert md to html
    for line in md_content:
        if line.strip() != "":
            # header
            match_header = re.compile(r'^(#{1,6})\s(.+)$',
                                      re.MULTILINE).match(line)
            if match_header:
                level = len(match_header.group(1))
                text = match_header.group(2)
                html_content.append(f'<h{level}>{text}</h{level}>')
            # unordered-list
            match_ordered_list = re.compile(r'^(-{1})\s(.+)$',
                                            re.MULTILINE).match(line)
            if match_ordered_list:
                list_text = match_ordered_list.group(2)
                list_item.append(f'<li>{list_text}</li>')

    # write in output file
    with open(output_file, 'w') as html_file:
        if html_content != []:
            for header_line in html_content:
                html_file.write(f'{header_line}\n')
        if len(list_item) != 1:
            for list_line in list_item:
                if list_line == '<ul>':
                    html_file.write(f'{list_line}\n')
                html_file.write(f'{list_line.strip()}\n')
                print(list_line)
            html_file.write('</ul>')

    exit(0)
