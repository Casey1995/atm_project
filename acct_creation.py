
import db
from datetime import date
import mysql.connector
from mysql.connector import errorcode
import logging
import getpass as p


def createAccount():
	user_name = db.query_db(db.check_customer_username)
	#check_customer_username = ("SELECT username FROM atm.customer;")

	fullname = input('Enter your fullname: ').title()

	newuser = input('Enter a unique login username: ')
	while newuser in user_name:
		print('Not available! use another name')
		newuser = input('Enter a unique login username again: ')

	pd = p.getpass(prompt='Enter a login password:')

	gender = input('Gender! Enter either "M" or "F" only: ').upper()

	email = input('Enter a valid email address: ')

	dob = input('Enter dte of birth in this format YYYY MM DD: ')
	dob = dob.split(' ')
	dob[0] = int(dob[0])
	dob[1] = int(dob[1])
	dob[2] = int(dob[2])
	#(dob[0],dob[1],dob[2])
	
	db.query_db(db.insert_cusomer_data_query,fullname, newuser, pd, gender, email, date(dob[0],dob[1],dob[2]))

	balance = int(input('Enter your opening balance: '))

	account_type = input('Enter account type,"Savings" or "Current": ').title()

	account_number = db.query_db(db.get_account_query,newuser, pd)[0][0]

	db.query_db(db.insert_account_data_query, account_number, balance, account_type)
	print('Welcome to WONDER BANK'.center(60))

#createAccount()
