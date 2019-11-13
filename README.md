# dirbrute
a simple, multithreaded python script to quickly scan for directories, parameter names and values

usage:
```
./dirbrute.py <url> <wordlist> <threads> [extensions]
./dirbrute.py http://example.com wordlist.txt 10 .php
```

It can also be used to brute force parameter names and values. 
e.g.

`./dirbrute.py 'http://example.com/action.php?' wordlist.txt 5 '=1'`

will bruteforce action.php?\<param\_name\>=1

`./dirbrute.py 'http://example.com/index.php?name=' wordlist.txt 5`

will bruteforce for values of `name`.

if you find any bugs please raise an issue!

### Why another one of these?
A bit of re-inventing the wheel helps to learn how tools work and simplify things.

Also, minimal things are fast.


### Where to find wordlists?
see https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content
