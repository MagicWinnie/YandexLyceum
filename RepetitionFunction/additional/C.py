def catch_flies(*args, func=None):
    pts = sorted(list(args), key=lambda x: (x['x'], x['y']))
    pts_new = []
    for pt in pts:
        if func is None:
            pts_new.append(pt)
        elif func(pt['x'], pt['y']):
            pts_new.append(pt)
    x_min = min(pts_new, key=lambda x: x['x'])['x']
    y_min = min(pts_new, key=lambda x: x['y'])['y']
    x_max = max(pts_new, key=lambda x: x['x'])['x']
    y_max = max(pts_new, key=lambda x: x['y'])['y']
    
    return ({'x': x_min, 'y': y_max}, {'x': x_max, 'y': y_min})

data = [{'x': 0, 'y': 0}, {'x': -5, 'y': 3}, {'x': 2, 'y': 11},
        {'x': 1, 'y': 5}, {'x': 2, 'y': 4}, {'x': -2, 'y': -2}]
print(*catch_flies(*data,
                   func=lambda x, y: -3 < x < 10 and
                                     -2 < y < 10), sep='\n')