

def forElse():
    my_list=["apple0","banana"]
    for i in my_list:
        if i=="banana":
            break
    else:
        raise ValueError("No Banana")

if __name__=="__main__":
    forElse()
