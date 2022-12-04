#!/usr/local/bin/python3
"""
This script will get AoC statement and create puzzle and example input files, 
as well as solution stubs

By default it will try to get the last day of the current AoC using your
cookies (you'll need to export them from the browser in Netscape format to
cookies.txt using some browser extensionz). 

Will create a separate problem folder with: 
* stub Part 1, and if available, Part 2 solution files with problem statement 
  in comments, 
* create a README.md from the statements.
* write all <pre><code> examples to separate files so you can feed them to your
  soluion as test inputs
* save your personal puzzle input

    dd-problem-name/1-daydd-problem-name.py
    dd-problem-name/2-daydd-problem-name.py
    dd-problem-name/README.md
    dd-problem-name/input
    dd-problem-name/ex1, etc.
    
File and dir names were chosen for easy cmdline autocomplete, you can customize them
"""

import sys, re, os, datetime, requests, http, bs4, argparse, subprocess
from os.path import exists

DIR_NAME = '{day_number:02d}-{title}'
STUB_NAME = '{part}-day{day_number:02d}-{title}.py'
EXAMPLE_NAME = 'ex{ex_number}'
INPUT_NAME = 'input'

STUB_TEMPLATE = 'import sys\n\nanswer = 0\nfor line in sys.stdin:\n    ans += 1\n\nprint(answer)\n'

BASE_URL = 'https://adventofcode.com'
HEADERS = 'accept: text/html\naccept-encoding: gzip, deflate, br\naccept-language: en-US,en\ncache-control: max-age=0\nsec-ch-ua: "Google Chrome";v="100", "Chromium";v="100", "Not=A?Brand";v="555"\nsec-ch-ua-mobile: ?0\nsec-fetch-dest: document\nsec-fetch-mode: navigate\nsec-fetch-site: none\nsec-fetch-user: ?1\nupgrade-insecure-requests: 1\nuser-agent: Mozilla/5.0 Chrome Python Script'

def main():
    init()    

    global problem_dir, day
    
    day_url = get_day_url()
    day_number = day
    html = soup(get_url(day_url))

    statements = html.select('main article')
    title = get_problem_title(statements[0])
    problem_dir = DIR_NAME.format(**locals())

    if not exists(problem_dir):        
        os.mkdir(problem_dir)
    elif not os.path.isdir(problem_dir):
        raise FileExistsError(f"Problem directory {problem_dir} cannot be created: file exists and is not a dir")

    ex_number = 0
    
    for i, statement in enumerate(statements):
        part = i+1
        stub_fn = render_fn_template(STUB_NAME, locals())
        if not exists(stub_fn):
            create_solution_stub(statement, stub_fn)
        
        examples = statement.select('pre code')
        for example in examples:
            ex_number += 1
            ex_fn = render_fn_template(EXAMPLE_NAME, locals())
            if not exists(ex_fn):
                open(ex_fn, 'w').write(example.decode_contents())

    input_fn = render_fn_template(INPUT_NAME, locals())
    if not exists(input_fn):
        data = get_url(f'{BASE_URL}/{year}/day/{day}/input')
        open(input_fn, 'wb').write(data)

    subprocess.Popen(["subl", stub_fn])

def init():
    global headers, cookies, year, day

    headers = dict([line.split(': ') for line in HEADERS.split('\n')])

    now = datetime.datetime.now()
    current_year = now.year if now.month==12 else now.year-1
    
    parser = argparse.ArgumentParser(prog = 'get_aoc_problem', description = 'Download AoC problem statments and puzzle data')
    parser.add_argument('day', type=int, nargs='?', default=0, help='default is last open day')
    parser.add_argument('-y', '--year', type=int, default=current_year, help=f'currently {current_year} by default')
    parser.add_argument('-c', '--cookies', type=str, metavar='FILE', default='cookies.txt', help='cookie file in Netscape format, save from your browser with an extension, default is cookies.txt')
    args = parser.parse_args()
    year, day = args.year, args.day

    cookies = http.cookiejar.MozillaCookieJar(args.cookies)
    cookies.load()
    cookies = requests.utils.dict_from_cookiejar(cookies)

def get_day_url():
    global day, year
    if day == 0:
        html = soup(get_url(f'{BASE_URL}/{year}'))
        day_path = html.select('pre.calendar a')[0].attrs['href']
        day = int(day_path[day_path.rindex('/')+1:])
        day_url = BASE_URL + day_path 
    else:
        day_url = f'{BASE_URL}/{year}/day/{day}'
    return day_url

def render_fn_template(template, vars):
    return os.path.join(problem_dir, template.format(**vars))

def get_problem_title(statement):
    title_pattern = re.compile(r'Day \d+: (.+[^ \-]) *-+')
    title = statement.select('h2')[0].decode_contents()
    title = title_pattern.search(title).group(1)
    return '-'.join( title.split()).lower()

def to_markdown(tag):
    """ Quick-and-dirty conversion from HTML to Markdown, should about do it for AoC pages """
    HTML2MD = {'em': '*', 'ex': '*', 'strong':'**', 'b': '**', 'h2':('## ', ''),
           'code': '`', 'p': ('\n',''), 'li':('* ',''), 'ul': ''}

    if tag.name in HTML2MD:
        delim = HTML2MD[tag.name]
        if type(delim)==str: delim = (delim, delim)
        return delim[0] + ''.join([to_markdown(child) for child in tag.children]) + delim[1]
    elif tag.name is None:
        return str(tag)
    else:
        return ''.join([to_markdown(child) for child in tag.children])

def create_solution_stub(statement, fn):
    statement_markdown = to_markdown(statement).replace('\n\n\n', '\n\n')
    open(fn, 'w').write(f'"""{statement_markdown}"""\n{STUB_TEMPLATE}')
    
    readme_fn = os.path.join(problem_dir, 'README.md')
    open(readme_fn, 'a' if exists(readme_fn) else 'w').write(statement_markdown)

def get_url(url):
    r = requests.get(url, headers=headers, cookies=cookies)    
    if r.status_code == 200:
        return r.content
    else:
        raise RuntimeError(f'Getting URL {url} failed, check address and connection')

def soup(content):
    return bs4.BeautifulSoup(content, 'html.parser')

if __name__ == '__main__':
    main()