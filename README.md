# CopyPasteCache
manager for Windows.

## The idea behind the project
Implement a cache manager which will allow me to copy and paste cached data. Clipboard copy/paste will be implemented using pyperclip.
The cache manager uses a secure DB [really?]

### Dev design [Currently implementing]  
1.	UI:  
	1.1	Windows tray icon  
		1.1.1	Right click : settings menu -> [Settings [1.2], about[1.3], close]  
		1.1.2	Left click menu : cache list -> [Up to X]  
	1.2	Settings menu:  
		1.2.1	Number of cached objects  
		1.2.2	Key mapping  
		1.2.3	Cache auto clean  
		1.2.4	DB path  
	1.3	About menu:  
		1.3.1	Short description about app and author.  
2.	DB:  
	2.1	key-value secure DB [pickleDB?]  
3.	Keyboard mapping
