# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:07:23 2018

@author: UttamSinha
"""

'''def train : 
    total = 0
	numspam = 0
	for email in train_data
		if email.label == SPAM: 
			numspam += 1
		total += 1
		processEmail(email.body, email.label)
	pA = numspam/(float)total
	pNotA = (total - numspam)/(float)total
'''

def processEmail(body, label):
	for word in body:
		if label == SPAM:
			trainPositive[word] = trainPositive.get(word, 0) + 1
			positiveTotal += 1
		else: 
			trainNegative[word] = trainNegative.get(word, 0) +1
			negativeTotal += 1

def conditional_word(word, spam):
"""This function helps give us the conditional probability p(B_i | A_x)"""
	if spam: 
		return trainPositive[word]/(float)positiveTotal
	return trainNegative[word]/(float)negativeTotal

def conditional_email(body, spam)
"""THis function helps give us the conditional probability p(B | A_x)"""
	result = 1.0
	for word in body: 
		result *= conditional_word(word, spam)
	return result


def classify(email)
""" This last function defiens the email as either spam or not spam"""
	isSpam = pA * conditional_email(email, True)
	notSpam = pNotA * conditional_email(email, False)
	return isSpam > notSpam
