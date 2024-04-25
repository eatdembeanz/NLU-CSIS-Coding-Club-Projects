import globalvariables
def start():
    print("Section2 starts")
    print("updated name is",globalvariables.name)
    if globalvariables.name == "jimmy":
        print("Section 3 starts!")
        import section3
        section3.start()
    else:
        print("Section 4 starts!")
        import section4
        section4.start()