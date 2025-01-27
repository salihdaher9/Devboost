def total_salaries(people):
    return sum([p["salary"] for p in people])


def total_salaries_for_position(people, position):
    # ---- YOUR CODE HERE -----------------
    return sum([p["salary"] for p in people if p["position"]==position])

    # -------------------------------------