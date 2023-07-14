def study_schedule(permanence_period, target_time):
    hour_repeat = 0
    if target_time is None or permanence_period is None:
        return None
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            hour_repeat += 1
    return hour_repeat

    raise NotImplementedError
