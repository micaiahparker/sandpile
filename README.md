[![Build Status](https://travis-ci.org/micaiahparker/sandpile.svg?branch=master)](https://travis-ci.org/micaiahparker/sandpile)

# sandpile
Python representation of Sandpiles as described by  Numberphile [here](https://www.youtube.com/watch?v=1MtEUErz7Gg)


## Example
```python
>>> from sandpile import Sandpile, MaxSandpile

>>> print(Sandpile(3, 4, fill=1))
> 1 1 1 1
> 1 1 1 1
> 1 1 1 1


>>> pile = Sandpile.from_list([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
>>> print(pile)
> 0 1 0
> 1 0 1
> 0 1 0

>>> print(pile + MaxSandpile())
> 1 3 1
> 3 3 3
> 1 3 1


```

## Installation

```
pip install sandpile
```

For development be sure to install `pytest`.

## Requirements

* Python 3.3+

## TODO

Add algorithm for finding the identity of a set of grids.
