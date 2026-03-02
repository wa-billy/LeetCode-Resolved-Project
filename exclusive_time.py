def exclusiveTime(n: int, logs: list[str]) -> list[int]:
    result, stack, prev = [0] * n, [], 0
    for log in logs:
        _id, _type, time = log.split(':')
        _id, time = int(_id), int(time)
        if _type == 'start':
            if stack:
                result[stack[-1]] += time - prev
                prev = time
            else:
                result[stack.pop()] += time - prev + 1
                prev = time + 1