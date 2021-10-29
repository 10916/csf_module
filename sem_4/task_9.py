# Write a program that will ask to input the module name and number of
# components on the module with corresponding weighting. It should also ask to
# enter mark for the components and show you the final mark.
# Additionally you may include a feature, where user can input the desired overall
# mark for the module and program outputs the required marks for the components.
# Save it it in seminar4/ folder
# Push your updates to Github repository.


user_choice = input("Hello. If you want to calculate your final mark type 1. If you want to know what mark you should get for a specific final mark press 2. ")

if (user_choice == "1"):
    module_name = input("Type the name of your module. ")
    components_number = input("Type the number of assessment components. ")
    if (components_number == "1"):
        final_mark = input("Type your mark. ")
        print(f"Your final mark is: {final_mark}.(Lmao)") 
    elif (components_number == "2"):
        component_one = input("Type the weighting of the first assessment component. ")
        component_two = input("Type the weighting of the second assessment component. ")
        mark_one = input("Type your mark for the first assessment component. ")
        mark_two = input("Type your mark of the second assessment component. ")
        final_mark = (int(component_one) * int(mark_one) + int(component_two) * int(mark_two)) / 100
        print(f"Your final mark for {module_name} is: {final_mark}")
elif (user_choice == "2"):
    components_number = input("Type the number of assessment components. ")
    if (components_number == "1"):
        final_mark = input("Type the mark you want to get. ")
        print(f"Your should get: {final_mark}") 
    elif (components_number == "2"):
        component_one = input("Type the weighting of the first assessment component. ")
        component_two = input("Type the weighting of the second assessment component. ")
        mark_one = input("Type a mark you could get for the first component. ")
        final_mark = input("Type the mark you want to get. ")
        mark_two = (int(final_mark) * 100 - int(component_one) * int(mark_one))/int(component_two)
        print(f"You should get {int(mark_two)} for second assessment to get {final_mark}.") 
        if (mark_two > 100):
            print("(Be realistic, lol)")
    