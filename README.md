# Arlo-Camera-ModeChangeServer
A simple server to change the mode of your arlo camera

To make this run you will need to run the following commands on a minimal debian / minibian server:

apt-get install python-setuptools

pip install selenium

apt-get install xvfb

apt-get install iceweasel

pip install bottle


Then edit the ArloCamerasAllOn.py file and add your username and password these are in the file as *** USERNAME *** and *** PASSWORD *** where you need to change them.

then you can run with 

Xvfb :99 -ac &

export DISPLAY=:99

python ArloCamerasAllOn.py 

you should then get something like:

Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:8080/

this is then accessible from anywhere that can access your server on port 8080 which you can change in the .py file at the bottom if needed.

You then need to forward ports on your router and set up an account on no-ip / dyndns or similar if you have a dynamic IP.

Once that is done you can set up a maker channel on IFTTT and point it at

http://Your-Forwarded-Domain.com:8080/mode0

through to 

http://Your-Forwarded-Domain.com:8080/mode9

to switch modes as they show up in your arlo account on the website (not the app).

Also I would recommend setting up an account on arlo specifically for this as when it runs it will log you out of arlo which can be a bit annoying.
