""" 
/*
	* This program is free software: you can redistribute it and/or modify
	* it under the terms of the GNU General Public License as published by
	* the Free Software Foundation, either version 3 of the License, or
	* (at your option) any later version.
	*
	* This program is distributed in the hope that it will be useful,
	* but WITHOUT ANY WARRANTY; without even the implied warranty of
	* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	* GNU General Public License for more details.
	*
	* You should have received a copy of the GNU General Public License
	* along with this program. If not, see <https://www.gnu.org/licenses/>.
	*/
"""

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