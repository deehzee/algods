# Uses python3


def get_optimal_value(capacity, weights, values):
    densities = [v/w for v, w in zip(values, weights)]
    sorted_idx = sorted(list(range(len(weights))),
                        key=densities.__getitem__,
                        reverse=True)
    value = 0.0
    i = 0
    while capacity > 0 and i < len(weights):
        item = sorted_idx[i]
        w = min(capacity, weights[item])
        capacity -= w
        value += w * densities[item]
        i += 1
    return value


if __name__ == "__main__":
    n_items, capacity = map(int, input().split())
    values = []
    weights = []
    for _ in range(n_items):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    opt_val = get_optimal_value(capacity, weights, values)
    print(f'{opt_val:.10f}')

