# A One Dimension Gym Environment

The following is the most simple openAI Gym envoronment:
A one dimensional environment.
(there are many examples out there like this as this one [link](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa)).

(C) 2019 Stefan Edlich http://edlich.de

## Install
In the folder where the readme is, do:
```python
pip install -e .
```

In your code, look if it is registered correctly:
```python
 print(envs.registry.all())  # from gym import envs
```
(see https://gym.openai.com/docs/ at the end 'The Registry')

## USAGE
[-100, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]
list with 12 elements => Discrete(12)
There is a hole in 0 and beer in 8

Move Left = 0 and Right = 1 => Discrete(2)

