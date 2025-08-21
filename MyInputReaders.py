def read_string(prompt_msg):
	"""
	Purpose:
	Reads a string from user and removes leading and trailing whitespace.
	Parameters:
	prompt_msg (str): The message displayed to the user when prompting for
	input.
	Returns:
	str: The cleaned string entered by the user.
	"""
    
	return input(prompt_msg).strip()