def calculate_average(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(sum(marks) / len(marks), 2)
    return averages
def find_top_performer(averages):
    return max(averages, key=averages.get)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
average_marks = calculate_average(students)
top_performer = find_top_performer(average_marks)
print("Average Marks:", average_marks)
print(f'Top Performer: "{top_performer}"')
