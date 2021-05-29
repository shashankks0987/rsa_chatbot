# End to End encrypted chatroom
This is a pet project.
The project uses RSA algorithm to end-to-end encrypt all messsages. 
The server logs are printed and you can see the encrypted messages it recieves.
A public key is transmitted to the server at the start which distributes it to the other clients.

Setup:
1) Install python
2) Create a virtual envirnoment (venv or conda)
3) pip install keyboard
4) run python3 s1.py which is the server
5) run clients - python3  cl.py

First two texts you send will be setup texts where in server exchanges public keys.










Note: this project was written during college and might need a few tweaks
Feedback and contributions are welcome 
