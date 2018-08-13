#Use enumerate
my_container = ['Larry', 'Moe', 'Curly']
index = 0
print("Before:")
for element in my_container:
  print('{} {}'.format(index, element))
  index+=1
print("After:")
for index, element in enumerate(my_container):
  print('{} {}'.format(index, element))


# for else:
"""
for user in get_all_users():
	print('Checking {}'.format(user))
	for email_address in user.get_all_email_addresses():
		if email_is_malformed(email_address):
			print('Has a malformed email address!')
			break
	else:
		print('All email addresses are valid!')
"""
