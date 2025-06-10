MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

# Variables (cont.)

## Aliasing Issue in Python

Every data, constant or not, has an identifier, stored as an integer in Python.
```python
>>> a = 1
>>> b = 1
>>> id(1)
140165965326288
>>> id(a)
140165965326288
>>> id(b)
140165965326288
```
If the data is mutable, then we have a problem:
```python
>>> a = ['a', 'b']
>>> b = a
>>> b[0] = 0
>>> a
[0, 'b']
```
<details>
    <summary>More Examples</summary>

```python
>>> a = 4
>>> b = [1, 2, 3, a]
>>> a = 8
>>> print(b)
[1, 2, 3, 4]  # This is even worse than the previous example
```
```python
>>> a = [1,2]
>>> b = [1,2,a]
>>> a
[1, 2]
>>> b
[1, 2, [1, 2]]
>>> a.append(3)
>>> b
[1, 2, [1, 2, 3]]
>>> a
[1, 2, 3]
```
</details>
