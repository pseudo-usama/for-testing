import pprint
from dataclasses import dataclass, astuple, asdict
import inspect


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str

def main():
    comment = Comment(1, 'My comment')
    print(comment)

    pprint(inspect.getmembers(comment, inspect.isfunction))


main() 