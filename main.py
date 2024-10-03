math_marks = int(input("Enter your Math's mark :"))
science_marks = int(input("Enter your Science's mark :"))
english_marks = int(input("Enter your English's mark :"))
bangla_marks = int(input("Enter your Bangla's mark :"))

sum = math_marks+science_marks+english_marks+bangla_marks

total_full_marks = 4 * 100
print("The total Mark is :" , sum)

percentege = (sum/total_full_marks) * 100
print("The percentege is :" , percentege)