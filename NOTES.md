# HW2 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?

#I added and implemented all the nessecary method for each of the 3 modules. I implemented custom exceptions in `errors.py`, seat and waitlist behavior in `Event`, and club commands in `Club`.

## What broke, and how did you fix it?

#My `Event.cancel()` initially removed the first person in seats and not nessecarily the named member, so I fixed `cancel()` and used remove(member) instead. I also corrected `Club.handle()` so that it properly catches ValueErrors as well.

## What would you do differently next time?

#I would probably try to run `python -m pytest` more frequently. perhaps during the implementation of every method. right now im only running pytest at the end and fixing the code from there. 