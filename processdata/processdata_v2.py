row_data = {}

with open('PaceData.csv') as paces:
    column_heading = paces.readline().strip().split(',')
    column_heading.pop(0)
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_heading)):
            inner_dict[row[i]] = column_heading[i]
        row_data[row_label] = inner_dict

distance_run = input('Enter the distance attempted:')
recorded_time = input('Enter the recorded time:')
predicted_distance = input('Enter the distance you want a prediction for:')

column_heading = row_data[distance_run][recorded_time]
prediction = [k for k in row_data[predicted_distance].keys() if row_data[predicted_distance][k] == column_heading]
print('The prediction is ' + str(prediction))