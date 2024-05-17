# WikipediaGame


## Installation

(these instructions should work under GNU/Linux and Macos and WSL)

Prerequisites: Python

```
git clone https://github.com/LukeMorissette/WikipediaGame.git
cd WikipediaGame

```

Starting the program:

```
./setup.sh
source venv/bin/activate
python backlinks.py

```

## Limitations

- You may need to use `pip3` or `pip`.
- You may need to use another env (/path/to/venv/Scripts/activate) if you are on Windows 

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.
- USER INPUT within `backlinks.py`
