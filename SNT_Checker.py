try:import random;from colorama import Fore;from requests import post
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
global x2,j
x2='[🖤] @TweakPY'
j='''
[☑️] NEW USER:︎︎
'''
def with_list():
	error,count,done=0,0,0
	try:file=open('user.txt', 'r')
	except FileNotFoundError:exit('[!] No users File Detected - Note users file must be in user.txt File ..')
	ID=''#telegram id
	token=''#telegram bot token
	if ID=='' or token=='':print('[!] No Token/id Detected ')
	while True:
		user=file.readline().split('\n')[0]
		ru=post(f'https://accounts.snapchat.com/accounts/get_username_suggestions',headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '57','content-type': 'application/x-www-form-urlencoded; charset=utf-8','cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.9984181.84984984; _gid=GA1.2.8898894.9489450; _gat_UA-41740027-4=1','origin': 'https://accounts.snapchat.com','referer': 'https://accounts.snapchat.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'same-origin','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'},data={'requested_username': user,'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}).text
		if '"status_code":"OK"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
			except:pass
			with open('Available.txt', 'a') as x:
				tl='[] NEW USER -->  '
				x.write(tl+user+'\n')
		elif '"status_code":"TAKEN"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_BEGIN"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_END"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"DELETED"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_SEPARATED"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
def without_list():
	count,done,error=0,0,0
	user=""
	lena=input('[?] Length: ');length=(int(lena))
	ID=''#telegram id
	token=''#telegram bot token
	if ID=='' or token=='':print('[!] No Token/id Detected ')
	chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
	while True:
		for user in range(1):
			user=""
			for item in range(length):
				user+=random.choice(chars)   
		ru=post(f'https://accounts.snapchat.com/accounts/get_username_suggestions',headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '57','content-type': 'application/x-www-form-urlencoded; charset=utf-8','cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1','origin': 'https://accounts.snapchat.com','referer': 'https://accounts.snapchat.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'same-origin','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'},data={'requested_username': user,'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}).text
		if '"status_code":"OK"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
			except:pass
			with open('Available.txt', 'a') as x:
				tl='[] NEW USER -->  '
				x.write(tl+user+'\n')
		elif '"status_code":"TAKEN"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_BEGIN"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_END"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"DELETED"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		elif '"status_code":"INVALID_SEPARATED"' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available *{done}*{Fore.RESET} | {Fore.RED} Not Available *{error}*{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count *{count}* {Fore.RESET}  ',end='')
			error+=1
			count+=1
print("""
███████╗███╗   ██╗████████╗    ██████╗██╗  ██╗
██╔════╝████╗  ██║╚══██╔══╝   ██╔════╝██║  ██║
███████╗██╔██╗ ██║   ██║█████╗██║     ███████║
╚════██║██║╚██╗██║   ██║╚════╝██║     ██╔══██║
███████║██║ ╚████║   ██║      ╚██████╗██║  ██║
╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝╚═╝  ╚═╝
             By @TweakPY @vv1ck                           
""")
TFV=int(input("[1] without List\n[2] with List\n---------------\nEnter > : "))
if TFV==1:without_list()
elif TFV==2:with_list()
else:exit('\n[!] Exit... \n\nBy @TweakPY - @vv1ck')
