#!/data/data/com.termux/files/usr/bin/python3

import PySimpleGUI as  sg

sg.theme('randon')

layout = [
		[sg.Text('Battery status')],
		[sg.Image('android.png')]
		]
window = sg.Window('Battery status', layout)
while True:
	event, values = window.read()
	if event == None:
		break

window.close()
