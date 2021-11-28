#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 02:58:28 2021

@author: abdul
"""

import pdfplumber
import re
import csv
import pandas as pd
from collections import namedtuple

import requests
pdf = pdfplumber.open('Araf.pdf')

page = pdf.pages[0]


text = page.extract_text()


Line = namedtuple('Line', 'Employee, Gender, Ministry, Designation,  Date_of_First_Appt,  Step, IPPIS_Number, Grade, Date_of_Birth, Bank_Name, PFA_Name, Account_Number,Tax_State, Location,Pension_PIN')
Employee =[]
Gender = []
Ministry =[]
Designation=[]
Date = []
step=[]
ippis=[]
emp=[]
birth= []
bank=[]
PFA =[]
Account =[]
tax=[]
Location = []
Pension=[]
line_items = []

for row in text.split('\n'):
    if row.startswith("Employee"):
        Employee = row.strip(",")[16:42]
        print(Employee)
        
    if row.startswith("Gender"):
        Gender = row.split()[1]
        print(Gender)
        
    if row.startswith("Ministry"):
        Ministry = row.strip(", ")[10:54]
        print(Ministry)
        
    if row.startswith("Designation"):
        Designation = row.strip(", ")[13:31]
        print(Designation)
        
    if row.startswith("Date of First Appt"):
        Date = row.split()[4]
        print(Date)
        
    if row.startswith("Step"):
        step = row.split()[1]
        print(step)
        
    if row.startswith("IPPIS  Number"):
        ippis = row.split()[2]
        print(ippis)
        
    if row.startswith("Employee Name:"):
        emp = row.split()[6]
        print(emp)
        
    if row.startswith("Date of Birth:"):
        birth = row.split()[3]
        print(birth)
        
    if row.startswith("Bank Name:"):
        bank = row.strip(", ")[11:35]
        print(bank)
        
        
    if row.startswith("Bank Branch   PFA Name:"):
        PFA = row.strip(", ")[24:]
        print(PFA)
        
    if row.startswith("Account Number"):
        Account = row.split()[2]
        print(Account)
        
        
    if row.startswith("Ministry"):
        tax = row.strip(",")[65:]
        print(tax)

        
    if row.startswith("Location"):
        Location = row.strip(", ")[10:16]
        print(Location)
        
    if row.startswith("Account Number:"):
        Pension = row.split()[6]
        print(Pension)
        
    
        
            
        
    line_items.append(Line(Employee, Gender, Ministry, Designation, Date, step,ippis, emp,birth,bank,PFA, Account, tax, Location, Pension))
    
    
df = pd.DataFrame(line_items)
single_row = df.loc[[35]]
single_row.to_excel('Araf.xlsx',  index = None, header=True)




print("**********************Executing************************")
print("Done File Created")