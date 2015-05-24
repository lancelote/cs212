[![Build Status](https://travis-ci.org/lancelote/cs212.svg)](https://travis-ci.org/lancelote/cs212)

# Design of Computer Programs

Code for [Design of Computer Programs](https://www.udacity.com/course/cs212) 
udacity course

## Projects Description
### Poker

- [Poker hands comparison algorithm](poker/main.py)
- [Poker hands stats calculation](poker/stat.py)
- [Assignment 1](poker/ps1.py)
- [Assignment 2](poker/ps2.py)

### Zebra

- [Zebra puzzle solver](zebra/main.py)
- [Debug functions](debug/main.py)
- [Time checker](time_stat/main.py)

## Cryptarithmetic

- [Cryptarithmetic puzzle solver](crypt_ar/main.py)

## Floor puzzle

-[Floor puzzle solver](floor/main.py)

## Package Dependencies

```bash
pip install -r requirements.txt
```

## Testing

Unit tests (`py.test`), acceptance tests (`behave`) and syntax validation (`pylint`):
```bash
paver <sub_project>
# poker, zebra, crypt_ar, floor
```