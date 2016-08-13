


import re

##############################Some validation rules#####################
def validateZip(zipcode=None):
	if zipcode is None:
		return False
	rule = '^[0-9]{5}(?:-[0-9]{4})?$'#########valid zipcode#############
	if re.match(rule,zipcode):
		return True
	else:
		return False

def validated(first='', last='', add1='', add2='', city='', state='', zip='', phone=''):

	invalidEntries = []

	if len(first) == 0:
		first = False
	if len(last) == 0:
		last = False
	if len(add1) == 0:
		add1 = False
	if len(add2) == 0:
		add2 = False
	if len(city) == 0:
		city = False
	if len(state) == 0:
		state = False
	if len(zip) == 0:
		zip = False
	if len(phone) == 0:
		phone = False




	###################### Validate first name############################
	try:
		if (first is not None) and len(first) > 0:
			first = True
		else:
			first=False
	except:
		first=False

	##################### Validate last name###################################
	try:
		if (last is not None) and len(last) > 0:
			last = True
		else:
			last=False
	except:
		last=False

	#################### Boolean for Either first or last name valid###################
	name = first or last

	if name is False:

		invalidEntries.append('Enter either first or last name')

	other = add1 or add2 or city or state or zip or phone

	if other is False:

		invalidEntries.append('Enter an additional field')
	validFlag = name and other
	return validFlag, invalidEntries
