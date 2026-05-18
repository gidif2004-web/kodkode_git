def merge_and_sort(tp1, tp2):
    merged_tp = tp1 + tp2
    sorted_tp = sorted(merged_tp)
    return tuple(sorted_tp)
