import random

def load_data(filename):
  all_data = []
  file = open(filename, 'r')
  for data in file:
    all_data.append(data.replace('\n', ''))
  return all_data

def populate(qty, collection):
  data = []
  for i in range(qty):
    data.append(collection[random.randint(0,len(collection)-1)])
  return data

def generate_marks(class_size, no_subjects):
  all_marks = []
  for student in range(class_size):
    marks = []
    for mark in range(no_subjects):
      marks.append(random.randint(1,100))
    all_marks.append(marks)
  return all_marks

all_nms = load_data('data/names.txt')
all_sbj = load_data('data/caie_subjects.txt')

ClassSize = 6                                       # >> size of class <<
SubjectNo = 8                                       # >> number of subjects <<
StudentName = populate(ClassSize, all_nms)          # >> names of students <<
Subjects = populate(SubjectNo, all_sbj)
StudentMark = generate_marks(ClassSize, SubjectNo)  # >> student marks for each subject <<
Distinction = 0
Merit = 0
Pass = 0
Fail = 0

for student in range(ClassSize):
  TotalMark = 0
  AvgMark = 0
  Grade = ''

  for subject in range(SubjectNo):
    TotalMark += StudentMark[student][subject]
  AvgMark = int(TotalMark / SubjectNo)

  if AvgMark >= 70:
    Grade = "Distinction"
    Distinction += 1
  elif AvgMark >= 55:
    Grade = "Merit"
    Merit += 1
  elif AvgMark >= 40:
    Grade = "Pass"
    Pass += 1
  else:
    Grade = "Fail"
    Fail += 1

  print(StudentName[student], ": Total: ", TotalMark, "| Average: ", AvgMark, "| Grade: ", Grade)

print("=" * 60)
print(f"Distinction: {Distinction} | Merit: {Merit} | Pass: {Pass} | Fail: {Fail}\n")