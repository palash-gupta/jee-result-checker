answerKeyFile = open("25jan_shift2.txt", 'r')
answerKey = {}

for i in answerKeyFile.readlines():
    t = i.split()
    answerKey[t[0]] = t[1]

correct = []
incorrect = []

with open("palash.txt", 'r') as f:
    for i in f.readlines():
        t = i.split()
        if answerKey[t[0]] == t[1]:
            correct.append(t[0])
        else:
            incorrect.append(t[0])

print(f"Total Score: {len(correct) * 4 - len(incorrect)}\n\nCorrect Answers: {correct}\n\nIncorrect Answers: {incorrect}")