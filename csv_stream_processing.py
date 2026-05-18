from io import StringIO

# =======================================
# Task 1.
# =======================================

# def task1(search, data):
#     io = StringIO(data)
#     header = io.readline()
#     columns = header.strip().split(',')

#     for key in search:
#         if key not in columns:
#             raise Exception('Key mismatch')

#     while True:
#         is_match = True
#         line = io.readline()
#         if line == '':
#             break
#         filtered_line = line.strip().split(',')

#         for key in search:
#             i = columns.index(key)
#             if filtered_line[i] != search[key]:
#                 is_match = False

#         if is_match:
#             i = columns.index('value')
#             return filtered_line[i]

#     return '-1'

# =======================================
# Task 2. Row Counter
# =======================================

# def count_denied(data):
#     io = StringIO(data)
#     counter = 0

#     while True:
#         line = io.readline()
#         if line == '':
#             break

#         clean_line = line.strip()
#         if clean_line == 'DENIED':
#             counter += 1

#     return counter

# log_data = "ALLOWED\nDENIED\nALLOWED\nDENIED\nDENIED"
# print(count_denied(log_data))

# =======================================
# Task 3. Log Filter
# =======================================

from io import StringIO

def counter_critical(data):
    counter = 0
    io = StringIO(data)

    while True:
        line = io.readline()
        if line == '':
            break

        clean_line = line.strip()
        if clean_line == 'CRITICAL':
            counter += 1

    return counter

server_logs = "INFO\nWARNING\nCRITICAL\nINFO\nCRITICAL"

result = counter_critical(server_logs)

print(result)