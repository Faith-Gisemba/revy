
# Write a python program that takes in a list of cars 
# cars = ['Ford','BMW','Volvo'] and returns a sorted list
def sorted_list(cars):
    sorting = sorted(cars)
    return sorting

cars = ['Ford', 'BMW', 'Volvo']
sorting = sorted_list(cars)
print(sorting)


# Write a python function that takes one arguement which is a list 
# fruit = ["apples","grapes","pineapple"] and removes the last fruit from the list then 
# Then returns the list without the removed fruit
def remove_last_fruit(fruit):
    fruit.pop()
    return fruit

fruit = ["Kiwi", "Rasberries", "Guava"]
updated = remove_last_fruit(fruit)
print(updated)


   