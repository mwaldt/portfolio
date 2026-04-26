# JavaScript

My notes on running and setting up on my current linux install.

## Installation (Arch)

1. Install `pacman -Syu nodejs npm`
1. Verify `node --version`
1. Install the creat-react-app tool `npm install -g create-react-app`
1. Verify `create-react-app --version`


## Create an app

1. To create a new web application run `create-react-app web-app`
1. To start npm you can run `cd web-app && npm start`
1. From here it is safe to stop the application and start more work on it
1. To make a systemd service file for the react app you will need to edit `/lib/systemd/system/react.service` and put something like the following in:
```
[Service]
Type=simple
User=root
Restart=on-failure
WorkingDirectory=/root/web-app
ExecStart=npm start -- --port=3000
```
