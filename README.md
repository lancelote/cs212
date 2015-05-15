[![Build Status](https://travis-ci.org/lancelote/cs212.svg)](https://travis-ci.org/lancelote/cs212)

# Design of Computer Programs

Code for [Design of Computer Programs](https://www.udacity.com/course/cs212) 
udacity course

## Projects Description
### Poker

- [Poker hands comparison algorithm](poker/main.py)
- [Poker hands stats calculation](poker/stat.py)
- [Assignment 1](poker/ps1)
- [Assignment 2](poker/ps2)

### Zebra

- [Zebra puzzle solver](zebra/main.py)

## Package Dependencies

```bash
pip install -r requirements.txt
```

## Testing

Unit tests (`py.test`), acceptance tests (`behave`) and syntax validation (`pylint`):
```bash
paver <sub_project>
# ex.: paver zebra
```