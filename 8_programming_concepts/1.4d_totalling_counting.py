# >> totalling and counting
'''
'''
# >> ----------------------------- << example code >>
import sys

people = ['Andrew','Nate','Patrick','Zen']
heights = [1.78, 1.89, 1.70, 1.68]
weights = [72, 66, 62, 59]

cohort_size = 0
total_heights = 0
total_weights = 0
tallest_height = 0
tallest_person = ''
shortest_height = float(sys.maxsize)
shortest_person = ''
heaviest_weight = 0
heaviest_person = ''
lightest_weight = sys.maxsize
lightest_person = ''

for i in people:
    total_heights += heights[cohort_size]
    total_weights += weights[cohort_size]

    if heights[cohort_size] > tallest_height:
        tallest_height = heights[cohort_size]
        tallest_person = i
    if heights[cohort_size] < shortest_height:
        shortest_height = heights[cohort_size]
        shortest_person = i

    if weights[cohort_size] > heaviest_weight:
        heaviest_weight = weights[cohort_size]
        heaviest_person = i
    if weights[cohort_size] < lightest_weight:
        lightest_weight = weights[cohort_size]
        lightest_person = i

    cohort_size += 1

average_height = total_heights / cohort_size
average_weight = total_weights / cohort_size

print(f"\nCombined height ({cohort_size} people) | {total_heights} metres")
print(f"Average height ({cohort_size} people) | {average_height} metres")
print("-" * 50)
print(f"{tallest_person} is the tallest at {tallest_height} metres")
print(f"{shortest_person} is the shortest at {shortest_height} metres")
print("=" * 50)
print(f"Combined weight ({cohort_size} people) | {total_weights} kilos")
print(f"Average weight ({cohort_size} people) | {average_weight} kilos")
print("-" * 50)
print(f"{heaviest_person} is the heaviest at {heaviest_weight} kilos")
print(f"{lightest_person} is the lightest at {lightest_weight} kilos\n")