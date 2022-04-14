# python-json-login
A simple Python script to interact with JSON

# Why did you make this?
Well, I was doing a Python class assignment at the univ. I discovered that using a JSON file would be simple yet efficient to save the data locally. To understand JSON and Python's dict type data, I made this script. Also, to get used to using Regular Expression :) And to know how to start a repository on Github.
# Can I use it?
Of course you can! However, don't really use it on your web server... passwords are saved unencrypted... (jk, you should use database to manage data on web server)

# How does it work?
## Check if 'signup.json' file exists locally
If signup.json file does not exist, it'll create for you.

## Signup
1. Get user ID: It uses `input()` function to get user input.
2. Check user ID: Check if user ID meets the criteria I've set.
<br>The criteria are 5-15 characters, lowercase alphabets, numbers, `_`, `.`
<br>First it'll check the length with `if`, second it'll check the criteria with regular expression.
3. Get user Password
4. Write the changes to signup.json

# Which Python module were used?
json and re
