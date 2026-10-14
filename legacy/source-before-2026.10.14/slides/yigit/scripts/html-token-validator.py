#!/usr/bin/env python3
"""Offline HTML token checks for the standalone slides skill (not visual QA)."""
import argparse
from html.parser import HTMLParser
import os
from pathlib import Path
import re


class Styles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_style = False
        self.styles = []

    def handle_starttag(self, tag, attrs):
        self.in_style = self.in_style or tag == 'style'
        self.styles.extend(value for name, value in attrs if name == 'style' and value)

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.styles.append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='*')
    parser.add_argument('--type', choices=['all', 'slides', 'infographics'], default='all')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--colors', action='store_true')
    parser.add_argument('--fix', action='store_true', help='Unsupported; review findings manually')
    args = parser.parse_args()
    if args.fix:
        parser.error('--fix is not implemented; no files were modified')
    root = Path(os.environ.get('DESIGN_SYSTEM_PROJECT_ROOT', Path.cwd())).resolve()
    token_file = root / 'assets' / 'design-tokens.css'
    tokens = token_file.read_text(encoding='utf-8') if token_file.is_file() else ''
    definitions = set(re.findall(r'(--[\w-]+)\s*:', tokens))
    if args.colors:
        if not token_file.is_file():
            parser.error(f'Token CSS not found: {token_file}')
        print('\n'.join(sorted(definitions)))
        return 0
    if args.files:
        files = [Path(name) for name in args.files]
    else:
        directories = {'slides': root / 'assets/designs/slides',
                       'infographics': root / 'assets/infographics'}
        selected = directories.values() if args.type == 'all' else [directories[args.type]]
        files = [file for directory in selected for file in directory.rglob('*.html')]
    if not files:
        print('No HTML files found; nothing was validated.')
        return 1
    failed = False
    for file in files:
        if not file.is_file():
            print(f'ERROR: file not found: {file}')
            failed = True
            continue
        document = Styles()
        document.feed(file.read_text(encoding='utf-8'))
        css = re.sub(r'/\*.*?\*/', '', '\n'.join(document.styles), flags=re.S)
        local = definitions | set(re.findall(r'(--[\w-]+)\s*:', css))
        # A fallback makes an otherwise undefined var valid CSS.
        required = set(re.findall(r'var\(\s*(--[\w-]+)\s*\)', css))
        missing = sorted(required - local)
        errors = [f'Undefined token {name}' for name in missing]
        # Ignore primitive custom-property declarations, where literals belong.
        declarations = re.sub(r'--[\w-]+\s*:[^;{}]+;?', '', css)
        if re.search(r'#[\da-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(', declarations):
            errors.append('Hardcoded color in component styles; review token usage')
        if not css:
            errors.append('No inline styles to validate; inspect linked stylesheets separately')
        print(f'{file}: {len(errors)} issue(s); static token check only')
        for error in errors:
            print(f'  {error}')
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
