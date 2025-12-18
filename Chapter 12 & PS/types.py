from typing import Tuple, List, Dict, Union
n : int = 5
name : str = "Azmet"

#List of integers
number: List[int] = [1,2,3,4,5]

#Tuple of a string and a integer
person: Tuple[str,int] = ("Alice",23)

#Dictionary with string keys and integer values
scores : Dict[str,int] = {"Alice": 90, "Bob":78}

#Union type for variablesnthat can hold multiple types
identifier: Union[int,str] = "ID124"
identifier = 12345


def sum(a : int ,b : int):
    return a+b

s = sum(1,2)
print(s)
