def cube_odd(nums: list[int | str | bool]) -> int | None:
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in nums):
        return None
    return sum([x ** 3 for x in nums if x % 2 != 0])
