import sys

while True:
 target_and_sentence = sys.stdin.readline().split()
 target = target_and_sentence[0]
 if target == '#': break
 count = 0
 for i in range(1,len(target_and_sentence)):
   count += target_and_sentence[i].lower().count(target)
 print (target, count)
 