# sandpile
Python representation of Sandpiles as described by  Numberphile [here](https://www.youtube.com/watch?v=1MtEUErz7Gg)


## Example
```python
>>> from sandpile import Sandpile, MaxSandpile

>>> pile = Sandpile([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
>>> print(pile)
> 0 1 0
> 1 0 1
> 0 1 0

>>> pile + MaxSandpile()
> 1 3 1
> 3 3 3
> 1 3 1


```
