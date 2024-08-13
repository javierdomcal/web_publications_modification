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

def create_post_files(entries, output_dir):
    # Organizar las entradas por año para asignar días correctamente
    entries_by_year = {}
    for entry in reversed(entries):
        year = entry.get('year', '')
        if year not in entries_by_year:
            entries_by_year[year] = []
        entries_by_year[year].append(entry)

    for year, entries in entries_by_year.items():
        for day, entry in enumerate(entries, start=1):
            url = entry.get('url', '')
            title = entry.get('title', 'No Title Available Yet')
            journal = entry.get('journal', 'No Journal Available Yet')
            authors = entry.get('author', 'No Authors Available Yet').split(',')
            volume = entry.get('volume', '')
            pages = entry.get('pages','')
            extra = entry.get('extra', '')
            n = entry.get('n', day)  # Asignar `n` o usar `day` si `n` no está disponible
            
            # Formato de fecha basado en año y número de publicación
            file_date = f"{year}-01-{day:02d}"
            sanitized_title = re.sub(r'[^\w]+', '-', title.lower())
            file_name = f"{file_date}-{sanitized_title}.md"
                        
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
n: {n}
---
"""

            with open(os.path.join(output_dir, file_name), 'w') as post_file:
                post_file.write(file_content)

if __name__ == "__main__":
    bibtex_file = './_data/publications.bib'
    output_dir = './_posts'  # Cambiar la salida a la carpeta _posts
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    bibtex_content = read_bibtex(bibtex_file)
    entries = parse_bibtex(bibtex_content)
    create_post_files(entries, output_dir)
