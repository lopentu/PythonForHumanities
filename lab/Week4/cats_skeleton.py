print("<prelude>")
print("<introduction>")

print("<choice>")
x_choice = input("(1 or 2) >> ")
if x_choice == "1":
    print("<skimbleshanks>")
    print("<kidnap>")
    print("<findme>")
    x_findme = input("(1 or 2) >> ")
    if x_findme == "1":
        print("<Mistoffelees>")
    elif x_findme == "2":
        print("<Macavity>")
        print("<End>")
        exit()
    else:
        exit()
elif x_choice == "2":
    print("")
else:
    exit()

print("<grizabella>")
print("<memory>")
print("<address>")

print("<End>")
