from dataclasses import dataclass
from typing import Optional


class Command:
    pass


@dataclass
class CreateMember(Command):
    name: str
    email: str
    team_id: Optional[int] = None


@dataclass
class DeleteMember(Command):
    id: int


# 다른 커맨드들...
