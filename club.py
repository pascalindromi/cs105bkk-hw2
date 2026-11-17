"""HW2 · club.py: the club and its chat bot. Practises Session 4 (each class has one job),
Session 5 (importing your own modules and the standard library) and Session 6 (catching only
the errors you expect)."""

from errors import AlreadySignedUpError, NotSignedUpError, SignupError, UnknownEventError
from event import Event


class Club:
    """A student club. It finds events by title; each Event looks after its own seats."""

    def __init__(self, name: str):
        """Provided: a club with no events yet."""
        self.name = name
        self.events: dict[str, Event] = {}

    def add_event(self, title: str, capacity: int) -> Event:
        if capacity <= 0 or title in list(self.events.keys()):
            raise ValueError()
        event = Event(title, capacity)
        self.events[title] = event
        return event

    def event(self, title: str) -> Event:
        if title in self.events.keys(): return self.events[title]
        else: raise UnknownEventError(title)

    def handle(self, line: str) -> str:
        try:
            command, title, name = line.split(", ")
            current_event = self.events[title]
            if command == "join":
                output = current_event.sign_up(name)
                if output == "waitlist":
                    return f"{name} is on the waitlist for {title}."
                return f"{name} has a seat at {title}."
            if command == "leave":
                output = current_event.cancel(name)
                if output == None:
                    return f"{name} left {title}."
                return f"{name} left {title}. {output} gets the seat."
            else:
                return f"Sorry, I don't understand '{command}'."
        except (NotSignedUpError, AlreadySignedUpError, UnknownEventError) as Err:
            return f"Sorry, {Err}."
        except ValueError:
            return f"Sorry, I don't understand '{line}'."

    def attendance(self) -> dict[str, int]:
        participants_list = {}
        for an_event in list(self.events.values()):
            for participants in an_event.seats:
                if participants not in participants_list:
                    participants_list[participants] = 1
                else:
                    participants_list[participants] += 1
        return participants_list


if __name__ == "__main__":
    # Provided: a short run of the chat bot. It runs only with `python club.py`, not on import.
    club = Club("Harbour.Space Bangkok club")
    club.add_event("Muay Thai basics", 2)
    for line in [
        "join, Muay Thai basics, Nino",
        "join, Muay Thai basics, Aung",
        "join, Muay Thai basics, Tashi",
        "leave, Muay Thai basics, Nino",
        "join, Chess night, Ploy",
    ]:
        print(club.handle(line))
