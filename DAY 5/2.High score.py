student_score = [56,25,48,123,48,569,785,156,456,223,486,321,694,556,52,49,77]
total_exam_score = sum(student_score)
print(total_exam_score)
print(max(student_score))

sum = 0
for score in student_score:
    sum += score
print(sum)

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max)




