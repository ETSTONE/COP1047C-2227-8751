#!/usr/bin/env python
# coding: utf-8

# In[6]:


tax_rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

gross_income = float(input('Enter the gross income: '))
number_dependents = int(input('Enter the number of dependents: '))

taxed_income = gross_income - (standard_deduction + (dependent_deduction * number_dependents))
income_tax = taxed_income * tax_rate

print('The income tax is $' + str(income_tax))
##Hope you make a lot of money this year that you don't need to worry about your taxes

