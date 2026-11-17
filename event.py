"""HW2 · event.py: one club event with limited seats. Practises Session 4 (a dataclass with
its own lists) and Session 6 (raising the club's exceptions)."""

from dataclasses import dataclass, field
from tkinter import N

from errors import AlreadySignedUpError, NotSignedUpError


@dataclass
class Event:
    """One event. Members in `seats` have a place; members in `waitlist` wait, first come first."""

    title: str
    capacity: int
    seats: list[str] = field(default_factory=list)
    waitlist: list[str] = field(default_factory=list)

    def seats_left(self) -> int:
        """Provided: how many seats are still free."""
        return self.capacity - len(self.seats)  

    def sign_up(self, member: str) -> str:
        if member in self.seats or member in self.waitlist:
            raise AlreadySignedUpError(member, self.title)
        if self.seats_left() > 0:
            self.seats.append(member)
            return "seat"
        self.waitlist.append(member)
        return "waitlist"
        

    def cancel(self, member: str) -> str | None:
        """Take the member off the event. Return who moves up from the waitlist, or None."""
        if len(self.seats) <= 0:
            raise NotSignedUpError(member, self.title)
        self.seats.pop(0)
        if len(self.waitlist) <= 0:
            moved_up = None
        else:
            moved_up = self.waitlist.pop(0)
            self.seats.append(moved_up)
        return moved_up


    def place(self, member: str) -> int:
        if member in self.seats:
            return 0
        elif member in self.waitlist:
            return self.waitlist.index(member) + 1
        else:
            raise NotSignedUpError(member, self.title)
