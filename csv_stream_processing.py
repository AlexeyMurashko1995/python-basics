from io import StringIO

# =======================================
# Task 1.
# =======================================

def task1(search, data):
    io = StringIO(data)
    header = io.readline()
    columns = header.strip().split(',')

    for key in search:
        if key not in columns:
            raise Exception('Key mismatch')

    while True:
        is_match = True
        line = io.readline()
        if line == '':
            break
        filtered_line = line.strip().split(',')

        for key in search:
            i = columns.index(key)
            if filtered_line[i] != search[key]:
                is_match = False

        if is_match:
            i = columns.index('value')
            return filtered_line[i]

    return '-1'
