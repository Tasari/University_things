#%%
from variable import variable

variables_amount = 8

#All variables
a, s, b, t, l, e, x, d = (i for i in range(variables_amount))
list_of_variables = [a, s, b, t, l, e, x, d] 

#String(List) of all variables for easier filling
string_variables_list = 'asbtlexd'

'''
States of variables, i decided we can divide all variables into negative
and positive state, it enables easier filling of initial table.
e.g. Smoker? Positive (Smokes), Lung Cancer? Negative(Not ill)
'''
negative, positive = (0, 1)

clinic_variables = [variable(
   letter, [negative, positive]
   ) for letter in string_variables_list]

#Check if variable Clinic_variables[var].name = "var", to assert valid assigning
for variable, variable_str in zip(list_of_variables, string_variables_list):
   assert(clinic_variables[variable].name == variable_str)
   assert(clinic_variables[variable].domain == [0, 1])