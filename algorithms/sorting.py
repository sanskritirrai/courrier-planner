def merge_sort(parcels):
    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_priority = int(left[i]["priority"])
        right_priority = int(right[j]["priority"])

        if left_priority > right_priority:
            result.append(left[i])
            i += 1
        elif left_priority < right_priority:
            result.append(right[j])
            j += 1
        else:
            if left[i]["deadline"] <= right[j]["deadline"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result