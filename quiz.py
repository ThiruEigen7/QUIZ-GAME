questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")
options =  (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answer = ("C", "D", "A", "A", "B")
guesses = []
mark = 0
questionnum = 0

for question in questions:
    print("-----------")
    print(question)
    print("------------")
    for option in options[questionnum]:
        print(option)
    guess = input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answer[questionnum]:
        mark+=1
        print("coorect!")
    else:
        print("incorrect!")
    questionnum+=1
print("    RESULT     ")
print("----------------")
for answers in answer:
     print(answers,end=",")
print()
for score in guesses:
    print(score,end=",")
print()

mark = int(mark/len(questions)*100)
print(f"your score is :{mark}%")


