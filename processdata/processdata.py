row_data = {}

with open('PaceData.csv') as paces:
    column_heading = paces.readline().strip().split(',')
    column_heading.pop(0)
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        row_data[row_label] = row
    
    num_cols = len(column_heading)
    print(num_cols,end=' -> ')
    print(column_heading)

    num_2mi = len(row_data['2mi'])
    print(num_2mi,end=' -> ')
    print(row_data['2mi'])

    num_marathon = len(row_data['Marathon'])
    print(num_marathon,end=' -> ')
    print(row_data['Marathon'])