"""
    https://www.codewars.com/kata/626d691649cb3c7acd63457b/train/python
"""


def champion_rank(pilot: int, events: str) -> int:
    if len(events) == 0:
        return pilot

    pilots = [i + 1 for i in range(20)]
    events_arr = events.split(' ')
    tape = [(int(events_arr[i]), events_arr[i + 1]) for i in range(0, len(events_arr), 2)]

    for pilotid, evt in tape:
        idx = [ix for ix, v in enumerate(pilots) if v == pilotid][0]
        tmp_pilot = pilots.pop(idx)
        if evt == 'O':
            pilots.insert(idx - 1, tmp_pilot)

    return -1 if pilot not in pilots else [ix + 1 for ix, v in enumerate(pilots) if v == pilot][0]
