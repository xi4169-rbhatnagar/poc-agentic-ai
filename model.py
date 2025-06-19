import dataclasses
from typing import TypedDict, Annotated, List

from langgraph.graph import add_messages


@dataclasses.dataclass
class State:
    messages: Annotated[List, add_messages]
