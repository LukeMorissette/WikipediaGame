# WikipediaGame


## Installation

(these instructions should work under GNU/Linux and Macos and WSL)

Prerequisites: Python

```
git clone https://github.com/LukeMorissette/WikipediaGame.git
cd WikipediaGame


Starting the program:

```
pip install -r requirements.txt
source venv/bin/activate
python backlinks.py

```

## Limitations

- You may need to use `pip3` or `pip`.
- You may need to use another env (/path/to/venv/Scripts/activate) if you are on Windows 
- ...

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.

## Further Ideas

- Improve the efficiency of the search.
- Add heuristics for faster search.
- Use LLMs to make better guesses, resulting in faster search.
- ...

## Branches

- `version1` computes the shortest path betwen two wikipedia pages
- `version2` (=`main`) additionally displays all pages visited during the computation
- `dev` will output the pages being visited in real time (under development)
