paragraph = 'A young boy was playing with a ball in the street. He kicked it too hard, and it broke the window of a house and fell inside. A lady came to the window with the ball and shouted at the young boy, so he ran away, but he still wanted his ball back. A few minutes later he returned and knocked at the door of the house, and when the lady answered it, he said My father going to come and fix your window very soon. After a few more minutes a man came to the door with tools in his hand, so the lady let the boy take his ball away.'

paragraphList = paragraph.split(' ')
print(paragraphList)
print(len(paragraphList))

toBeSet = {'am', 'is', 'are', 'was', 'were'}
count = 0
for w in paragraphList:
    if w in toBeSet:
        count += 1
print(count)

wordUnique = set(paragraphList)
print(wordUnique)
print(len(wordUnique))

#end










