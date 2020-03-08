# M_UNO
multiplayer Uno Game developed in python language 
used:
- multithreading 
- server-client topology of network
- pygame

Contains:
# cards.py: 
contains the class Cards and every instance of Cards class is a Card object having different qualities/parameters.
# client.py:
handles the client side communication by binding the message to send and unbinding the recieved message.
# server.py:
server configuration file
# game.py:
on creation of object of Game class will initiate a room for the clients to come and connect with the server.
# gui.py:
define the different components of GUI of the client side game.
# player.py:
copntains the information of the players.
# network.py:
contains the information about network communication system. to configure it for your system u need to insert yout PCs wifi adapter IPv4 to the 8th line of this file https://github.com/yash-khandelwal/M_UNO/blob/1ee983854016c764a1d36747f6d4a052dd04fec7/network.py#L8.
