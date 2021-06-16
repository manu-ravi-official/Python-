import camelcase
input_st= input ("Ente Names :\n")
school= input_st.split()
print("The length of list is: ", len(school))
print("School names")
for name in school:
   # print(name)
    from camelcase import CamelCase
    c = camelcase.CamelCase()
    school1=c.hump(name)
    school2=school1.split()
    print(school2)
    #print()
#txt = "hello world"

def convert(lst):
    return (lst[0].split())
  
