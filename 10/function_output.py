
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs"
    f_name_title=f_name.title()
    l_name_title=l_name.title()
    #return f"{f_name_title} {l_name_title}"
    return f_name_title+" "+l_name_title
print(format_name("Hulusi","BehçeT"))
print(format_name(input("What's your first name?"),input("What's your last name?")))