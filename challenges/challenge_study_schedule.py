def study_schedule(permanence_period, target_time):
    try:    
        students_in_period = 0
        for index in permanence_period:
            if (target_time >= index[0] and target_time <= index[1]):
                students_in_period += 1
        return students_in_period
    except TypeError:
        return None