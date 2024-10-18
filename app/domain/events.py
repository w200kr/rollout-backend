from dataclasses import dataclass
from datetime import datetime


class Event:
    pass


@dataclass
class MemberCreated(Event):
    id: int
    name: str
    email: str
    created_at: datetime


# 다른 이벤트들...
