students={"rahul":85,"sathwik":86,"priya":92,"raju":79,"siri":93}
for name,score in students.items():
    total=0
    total+=score
average=total/len(students)
top_scorer=max(students)
bottom_scorer=min(students)
for name,score in students.items():
    if score==top_scorer:
        top_scorer=name
    if score==bottom_scorer:
        bottor_scorer=name
print("student grade book")
print("class average:",average)
print("top scorer:",top_scorer)
print("bottom scorer:",bottom_scorer)

