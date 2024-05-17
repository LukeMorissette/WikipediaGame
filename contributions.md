## Contributions

### Luke
- Completed the "Previous Work (BART AND WORDTOVEC IMPROVEMENT)" milestone, enhancing and optimizing previous work related to BART and Word2Vec.
- Created the setup and main development for the backtracking method.
- Conducted research on optimization techniques for the backtracking algorithm.
- Implemented initial versions of backtracking algorithms and fine-tuned parameters for improved performance.
- Collaborated to integrate backtracking improvements into the overall project structure.

### Kevan
- Assisted in brainstorming potential mistakes that the AI could make and proposed improvements.
- Contributed to the main development of a new backlink tracking mechanism.
- Implemented threading for improved efficiency.
- Conducted testing to ensure the functionality and reliability of the script.
- Contributed to submitting the project. 
- Created new documentation and code cleanup. 

## AI

We used Aider and ChatGPT for code generation (as advised in the project). 
We used ChatGPT to help us with code cleanup and debugging. 

# Notes
We switched our method and proposal throughout the project, so this is a different project than we started with, which was different from our original proposal. 

## Sample Input 1
- Starting article: "Artificial intelligence"
- Final article: "Machine learning"

Our algorithm: 

```
https://en.wikipedia.org/wiki/Artificial_intelligence
Please enter your starting article: ['https://en.wikipedia.org/wiki/User%3ABlankfrack/Books/Blankfrack_Programming', 'https://en.wikipedia.org/wiki/Sample_complexity', 'https://en.wikipedia.org/wiki/Talk%3ASampling_%28statistics%29/Archives/2012', 'https://en.wikipedia.org/wiki/User_talk%3AKIWSUMAP', 'https://en.wikipedia.org/wiki/Middle_Eastern_Americans', 'https://en.wikipedia.org/wiki/Talk%3AWolfram_Mathematica', 'https://en.wikipedia.org/wiki/User%3AAdarsh_shrinagesh/Books/2017PersonalAdarsh1', 'https://en.wikipedia.org/wiki/Jan_Peters_%28computer_scientist%29', 'https://en.wikipedia.org/wiki/User%3AMelomodiga/Books/Algorithms', 'https://en.wikipedia.org/wiki/Shane_Legg']
Machine learning
Found: https://en.wikipedia.org/wiki/Digital_library
Path found: ['https://en.wikipedia.org/wiki/Artificial_intelligence', 'https://en.wikipedia.org/wiki/Digital_library, https://en.wikipedia.org/wiki/Machine_learning']
Time taken: 2.3931972980499268 seconds

```

Previous version ()

```

Found finish page: https://en.wikipedia.org/wiki/Machine_learning
Search took 2.8347728252410889 seconds.
Discovered pages: 1224
Number of discovered pages: 1227

```

Our algorithm requires less tracking and is faster in different sample inputs such as `Artificial intelligence` and `Machine learning` as they represent common topics. 

## Sample Input 2
- Starting article: "Martin Wirsing"
- Final article: "Taylor Swift"

```
Found: https://en.wikipedia.org/wiki/King%27s_College_London
Path found: ['https://en.wikipedia.org/wiki/Martin_Wirsing', 'https://en.wikipedia.org/wiki/University_of_Passau', 'https://en.wikipedia.org/wiki/King%27s_College_London, https://en.wikipedia.org/wiki/Taylor_Swift']
Time taken: 5.958757162094116 seconds

```

Previous version ()

```

Martrin Wirsing to Taylor Swift: https://en.wikipedia.org/wiki/Martin_Wirsing https://en.wikipedia.org/wiki/Ludwig-Maximilians-Universität_München https://en.wikipedia.org/wiki/Konrad_Adenauer https://en.wikipedia.org/wiki/Taylor_Swift
Search took: 224 seconds
Discovered pages: 36676

```

## Sample Input 3
- Starting article: "Julius Caesar"
- Final article: "LeBron James"

```
Found: https://en.wikipedia.org/wiki/Laurence_Olivier
Path found: ['https://en.wikipedia.org/wiki/Julius_Caesar', 'https://en.wikipedia.org/wiki/Marcus_Licinius_Crassus', 'https://en.wikipedia.org/wiki/Laurence_Olivier, https://en.wikipedia.org/wiki/LeBron_James']
Time taken: 15.196425914764404 seconds

```

Previous version ()

```

Search exceeded time limit.
Elapsed time: 500.84365010261536

```
Our algorithm shows considerable improvements in the `Martin Wirsing` and `Taylor Swift` example, and `Julius Caesar` and `LeBron James` examples


## Improvement Comparison
The improvements proposed in the project aim to enhance the efficiency, accuracy, and reliability of the Wikipedia Path Finder script. By integrating caching, dynamic backlinks fetching, link extraction optimization, and robust error handling, significant improvements in performance and functionality are expected.

To quantify the improvements, metrics such as the reduction in API requests, decrease in execution time, and increase in path-finding accuracy can be measured and compared between the original and improved versions of the script.
