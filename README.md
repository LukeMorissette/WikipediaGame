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

# Future Work

Future work on the Wikipedia Path Finder script can be focused on several areas to further improve its efficiency, accuracy, and user experience. Here are some potential directions:

1. Advanced Caching Strategies
Description:
Implement more sophisticated caching mechanisms, such as:

LRU (Least Recently Used) Cache: This can help manage the memory usage effectively by discarding the least recently used data when the cache reaches its size limit.
Distributed Caching: Use distributed caching systems like Redis or Memcached to store backlinks and links across multiple nodes, enhancing performance in a scalable manner.

2. Graph Database Integration
Description:
Integrate a graph database (e.g., Neo4j) to store and query Wikipedia links. Graph databases are optimized for traversing relationships, which can significantly improve the path-finding process.

Implementation Considerations:
Neo4j Integration: Use the neo4j Python driver to connect and interact with a Neo4j database, storing Wikipedia articles and their backlinks as nodes and relationships.
Query Optimization: Optimize queries to ensure quick traversal of the graph, leveraging the inherent strengths of graph databases.

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.
- USER INPUT within `backlinks.py`
