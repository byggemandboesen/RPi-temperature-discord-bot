# RPi-tempereture-discord-bot
THIS CODE DOES NOT WORK ON ITS OWN!!

## Add an application in Discord developer
First add a new application in the Discord developer portal:
https://discord.com/developers/applications
Then create the bot and add the bot token to the code together with your desired command prefix.

Now add the bot to your desired server to test it.

## Run the code
Run the code on the raspberry pi by cd-ing to the dir of the code.

```bash
cd YOUR DIRECTORY
```

Then run the code:

```bash
python3 discord_bot.py
```

And then you can get the RPi temperature by typing your chosen command prefix followed by "cpu".
For example, if the prefix is '.' then you'd have to type '.cpu'.
