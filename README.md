![!img](./icons/Icon.png)



This Dead man switch encrypts a file and holds the keys in memory, the key will be kept in memory as long as you ping the switch telegram bot in the time interval you set the script to run at. You can also send a kill switch to destroy the key asap. There is also a reset switch keyword to stop the switch and decrypt the file and gracefully exit the switch.



TO RUN:

First, set the telegram bot token in the api.py. This should be the token to of the bot that you expect to ping. This key can be found from the [Bot Father](t.me/BotFather) bot in telegram. If there are no bots registered, one can be simply made from inside the Bot Father bot.

The switch can then be setup by executing the *switch.py* by simply running

```.....Dead_man_switch/$ python3 switch.py```

in the terminal.



Execute at your own risk!!