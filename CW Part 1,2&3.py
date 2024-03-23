# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

 
# Any code taken from other sources is referenced within my code solution.

# Student ID:w1953602 
 
# Date: 13/12/2022

pass_credits = 0
defer_credits = 0
fail_credits = 0
total = 0
decision = "y"
progress = 0
trailer = 0
retriever = 0
exclude = 0
total_outcome = 0
progress_1=[]
trailer_1=[]
ret =[]
ex =[]


def print_all():                                            #User-Defined Functions
    print()            
    print("-"*60)
    print("Histogram")                                      #Histogram
    print(f'Progress  {progress:02d} : {"*"*progress}')
    print(f'Trailer   {trailer:02d} : {"*"*trailer}')
    print(f'Retriever {retriever:02d} : {retriever*"*"}')
    print(f'Exclude   {exclude:02d} : {exclude*"*"}')
    print()
    total = progress + trailer + retriever + exclude
    print(total, "outcomes in total")
    print("-"*60)
    print()                           
    print(f"Progress                 -{tuple(progress_1)}") #Part 2 – List
    print(f"Progress (module trailer)-{tuple(trailer_1)}")
    print(f"Module retriever         -{tuple(ret)}")
    print(f"Exclude                  -{tuple(ex)}")
    file=open("20220130.txt", 'w')                          #Part 3 - Text File
    file.write(f"Progress                 -{tuple(progress_1)}\n")
    file.write(f"Progress (module trailer)-{tuple(trailer_1)}\n")    
    file.write(f"Module retriever         -{tuple(ret)}\n")   
    file.write(f"Exclude                  -{tuple(ex)}\n")
    file.close()
    return(print_all)

while decision == "y":
    mylist =[]
    try:
        pass_credits=int(input('Please enter your credits at pass: '))
        mylist.append(pass_credits)
    except:
        print('Integer required')
        continue
    if pass_credits not in range(0,121,20):
        print('Out of range.')
        continue
    try:
        defer_credits=int(input('Please enter your credit at defer: '))
        mylist.append(defer_credits)
    except:
        print('Integer required')
        continue
    if defer_credits not in range(0,121,20):
        print('Out of range.')
        continue
    try:
        fail_credits=int(input('Please enter your credits at fail: '))
        mylist.append(fail_credits)
    except:
        print('Integer required')
        continue
    if fail_credits not in range(0,121,20):
        print('Out of range.')
        continue
    total=pass_credits+defer_credits+fail_credits
    if total!=120:
        print('Total incorrect.')
        continue
    else:
        
        if pass_credits == 120:
            print("Progress")
            progress = progress + 1
            progress_1.append(mylist)
            
        elif pass_credits == 100:
            print("Progress (module trailer)")
            trailer = trailer + 1
            trailer_1.append(mylist)
            
        elif fail_credits >= 80:
            print("Exclude")
            exclude = exclude + 1
            ex.append(mylist)
               
        else:
            print("Module retriever")
            retriever = retriever + 1
            ret.append(mylist)
        while True:
            print()
            print("Would you like to enter another set of data ?")
            decision = input("Enter 'y' for yes or 'q' to quit and view results: ")
            if (decision == "q" or decision == "y"):
                break
            else:
                print('Please enter valid option')
                continue

print_all()




    
    
    

    
    
