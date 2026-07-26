total_chores=4
original_count= total_chores
print(f"you have {original_count} chores to finish today!\n")
 
completed_count=0
chore_number=1

while chore_number <= total_chores:
      
      if chore_number==1:
            next_chore="make your bed"
      elif chore_number==2:
            next_chore="feed the pet"
      elif chore_number==3:
            next_chore="take out the trash"
      else:
            next_chore="wash the dishes"
      answer = input(f"Have you finished:{next_chore}?(yes/no):")
      if answer=="yes":
            completed_count+=1
            chore_number+=1
            print("great job!chore completed.")
      else:
            print("okay,finish it and check again!")
      print("chores remaining:", total_chores - completed_count)
      print()

print("==== all chores complete!=====")
print("great work ")

test_value=0
safety_counter=0
while test_value<=0:
      print("it will run forever")
      safety_counter+=1
      if safety_counter==3:
            print("it will stop now")
            break
print("\n===== CHORE CHECKLIST SUMMARY =====")

print("Chores Assigned Today:", original_count)

print("Chores Completed:", completed_count)

print("Chores Remaining:", total_chores - completed_count)

print("======================================")