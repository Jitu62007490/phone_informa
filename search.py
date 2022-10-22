import pyfiglet as fgl
from googlesearch import search
res=fgl.figlet_format("RAJ",font="doh")
print(res)
#query=input("Enter your Target Name:-")
query=input("Enter Your Target Name |OR| Enter Your Target Phone No:-")
for i in search(query,tld="com",num=10,stop=10,pause=2):
    print(i)
