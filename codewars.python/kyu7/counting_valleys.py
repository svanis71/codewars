def counting_valleys(path: str) -> int:
    level, valley_count = 0, 0
    for d in path.replace('F', ''):
        level += (1 if d == 'U' else -1)
        valley_count += (1 if level == 0 and d == 'U' else 0)
    return valley_count
