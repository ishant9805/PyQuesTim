import time
from playsound import playsound

min_time_for_single_question = float(input("Enter the maximum time(in mins) you want to give at a question?"))
# whole_time_to_complete_the_paper = float(input("Enter the total time(in mins) you want to take?"))
no_of_questions_you_want_to_do = int(input('No. Of Questions you want to do: '))
time_required = no_of_questions_you_want_to_do * min_time_for_single_question


def timer1st(x):
	time.sleep(x * 60)
	playsound('ticktick.mp3')

print("Time Required: ", time_required)
print("Your time starts now.")

for _ in range(no_of_questions_you_want_to_do):
	timer1st(min_time_for_single_question)

playsound("timeOver.mp3")
print('Time\'s Up!!!!!!!!!!!!!!!!!!!!!')
