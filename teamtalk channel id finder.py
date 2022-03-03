import teamtalk, configparser, os
t = teamtalk.TeamTalkServer()

def Login():
	if not os.path.exists('config.ini'):
		hostAddress = input('enter host address')
		tcpport = input('enter tcp port')
		username = input('enter username')
		password = input('enter password')
		nickname = input('enter nickname')

		config_file = f"""
[options]
hostAddress = {hostAddress}
tcpport = {tcpport}
username = {username}
password = {password}
nickname = {nickname}
"""

		file_creation = open('config.ini', 'x', encoding = 'utf-8-sig')
		file_creation .write(config_file)
		print('config file created successfully.\nrun the program again.')
	else:
		try:
			config = configparser.ConfigParser()
			loaded = config.read('config.ini', encoding = 'utf-8-sig')
			host = config['options']['hostAddress']
			tcp = config['options']['tcpport']
			username = config['options']['username']
			password = config['options']['password']
			nickname = config['options']['nickname']
			t.set_connection_info(host, tcp)
			t.connect()
			t.login(nickname, username, password, 'clientName')
			saver = []
			channels = t.channels
			for channel in channels:
				destinationchannel = t.get_channel(channel['channel'])
				saver.append(f"channel name: {destinationchannel['channel']}\nchannel id: {destinationchannel['chanid']}")
			try:
				txt = open('channel lists.txt', 'x', encoding = 'utf-8-sig')
				txt.write('\n'.join(saver))
				txt.close()
				os.system('notepad.exe channel lists.txt')
			except:
				os.system('notepad.exe channel lists.txt')
		except:
			print('there is an error in config file\nremove it and run the program again.')

Login()