import re
import os

def read_bibtex(file_path):
    with open(file_path, 'r') as bib_file:
        content = bib_file.read()
    return content

def parse_bibtex(content):
    entries = content.split('@article')
    parsed_entries = []
    for entry in entries:
        if entry.strip():
            entry_dict = {}
            entry = entry.strip('{} \n')
            fields = re.findall(r'(\w+)\s*=\s*{(.*?)}', entry, re.DOTALL)
            for field in fields:
                entry_dict[field[0].strip()] = field[1].strip().replace('\n', ' ')
            parsed_entries.append(entry_dict)
    return parsed_entries

def create_html_files(entries, output_dir):
    num_entries = len(entries)
    for i, entry in enumerate(reversed(entries), start=1):
        url = entry.get('url', '')
        title = entry.get('title', 'No Title Available Yet')
        journal = entry.get('journal', 'No Journal Available Yet')
        authors = entry.get('author', 'No Authors Available Yet').split(',')
        year = entry.get('year', '')
        volume = entry.get('volume', '')
        pages = entry.get('pages','')
        extra = entry.get('extra', '')
        
        file_content = f"""---
layout: pub
exturl: "{url}"
title: "{title}"
authors:
"""
        for author in authors:
            file_content += f" - {author.strip()}\n"
        file_content += f"""journal: {journal}
year: {year}
extra: {extra}
volume: {volume}
pages: {pages}
n: {i}
---
"""

        with open(os.path.join(output_dir, f'pub_{i:03d}.html'), 'w') as html_file:
            html_file.write(file_content)

if __name__ == "__main__":
    bibtex_file = './_data/publications.bib'
    output_dir = './_publications'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    bibtex_content = read_bibtex(bibtex_file)
    entries = parse_bibtex(bibtex_content)
    create_html_files(entries, output_dir)
