def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry :("

s = input("Do you want program to shut down?").lower()

print(shut_down(s))

#somechange