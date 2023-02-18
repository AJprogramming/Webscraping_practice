import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
population = [39029342, 30029572, 22244823, 20448194]

new_list = [2, 4, 6, "California"]



# for state in states:
#     print(state + "\n" + "-------------")

# 1) first way to export data... No 3rd party library needed

with open('test.txt', 'w') as file:
    file.write("Data successufully scraped!")
    
# "open" function needs a 'filename' and 'mode'... "open" can have more than 2 operations
# the mode 'w' is for the right-mode, is the most used kind of mode
# In this function "open('test.txt', 'w')" is represented as file, so we don't need to write the whole thing again

# 2) second way to export data... w/ 3rd party

dict_states = {
    'states' : states,
    'population' : population
}

df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_csv('states_testing.csv', index=False)

# set index to False if I don't want to include it in the .csv

# 3) how to handle exception errors

for i in new_list:
    try:
        print(i/2)
    except:
        print('Element is not a number')
# an error comes up becomes we are tring to divide a string,'California'. To fix this add 'try'
# we want to use 'try' and 'except' because we don't want the whole code to break because of a single element

