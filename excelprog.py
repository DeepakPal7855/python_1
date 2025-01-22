import csv
data = [
     ["Name", "age", "Occupation"],
     ["Alice", 12, "Engineer"],
     ["Babli", 53, "Designer"],
     ["Charlie", 32, "Teacher"]
]
with open('output.csv', mode='w', newline='')as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)
print("Data written to 'output.csv' successfully.")
