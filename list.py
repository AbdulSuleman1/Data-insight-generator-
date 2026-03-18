my_properties = ["house","phone","car","plane"]
#print(my_properties[1])
my_properties[-3]="laptop"
my_properties[1:]=["cup","jug","van"]
my_properties.insert(2,"laptop")
my_properties.pop(2)
print(my_properties)
my_books = list(("english","maths","stat","computer"))
my_books.extend(my_properties)# to add to list together
my_books.sort(reverse=True)#desending order while for ascending just sort()
print(my_books)

cat =[36,"dog",637]
van = [83,"nich","piss",989]
tt = cat+van
print(tt)
