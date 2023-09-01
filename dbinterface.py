import sqlite3

def increment_strikes(username):
	conn = sqlite3.connect('mydatabase.db')
	cursor = conn.cursor()
	cursor.execute(f'''
		UPDATE users
		SET strikes = strikes + 1
		WHERE username = '{username}';
	''')
	conn.commit()
	conn.close()

def reset_strikes(username):
	conn = sqlite3.connect('mydatabase.db')
	cursor = conn.cursor()
	cursor.execute(f'''
		UPDATE users
		SET strikes = 0
		WHERE username = '{username}';
	''')
	conn.commit()
	conn.close()

def get_strikes(username):
	conn = sqlite3.connect('mydatabase.db')
	cursor = conn.cursor()
	a = cursor.execute(f'''
		GET strikes FROM users WHERE username = '{username}';
	''')
	conn.commit()
	conn.close()
	return a

def bal2xp(username, balcost, xpadd):
	conn = sqlite3.connect('mydatabase.db')
	cursor = conn.cursor()
	cursor.execute(f'''
		UPDATE users SET balance = balance - '{balcost}' WHERE username = '{username}';
		UPDATE users SET xp = xp + '{xpadd}' WHERE username = '{username}';
	''')
	conn.commit()
	conn.close()

increment_strikes('meme_d')
reset_strikes('meme_d')