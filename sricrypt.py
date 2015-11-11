#!/usr/bin/env python
import math
new_string=[]
dec=[]
def substitute(ch):
	temp = ord(ch) 
	temp=temp-96
	temp=temp+5
	val = int(math.fmod(temp,26))
	val=val+96
	oc=chr(val)
	new_string.append(oc)
def resub(ch2):
	temp=ord(ch2)
	temp=temp-96
	temp=temp-5
	val=int(math.fmod(temp,26))
	val=val+96
	oc2=chr(val)
	dec.append(oc2)
def sri_crypt(message):
	message=list(message)
	for char in message:
		substitute(char)
def sri_decrypt(message):
	message=list(message)
	for char in message:
		resub(char)
def custom_enc(message):
	sri_crypt(message)
	round1=''.join(new_string)
	sri_crypt(round1)
	round2=''.join(new_string)
	sri_crypt(round2)
	round3=''.join(new_string)
	l=len(round3)
	m=len(message)
	return round3[:m]
def custom_dec(a):
	sri_decrypt(a)
	dec_value=''.join(dec)
	sri_decrypt(dec_value)
	dec_value2=''.join(dec)
	sri_decrypt(dec_value2)
	dec_value3=''.join(dec)
	m=len(a)
	return dec_value3[:m]
