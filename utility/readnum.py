#!/usr/bin/python
#coding=utf8
import os

Decinal_Num = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

def analyze_one_line(line):
	for char in line:
#		Decinal_Num[int(char)] += 1
		if char != ' ' and char != '\t' and char != '\r' and char != '\n':
			Decinal_Num[int(char)] += 1

def analyze_number_string():
	f = open("./test.log");
	for line in f:
		analyze_one_line(line)

def output_result():
	for item in Decinal_Num:
		print item,Decinal_Num[item]

if __name__=="__main__":
	analyze_number_string()
	output_result()
