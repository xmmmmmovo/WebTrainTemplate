from dataclasses import dataclass


@dataclass
class Post:
    id: int
    author: int
    title: str
    content: str
    gen_time: int
    modify_time: int
