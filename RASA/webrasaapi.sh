source rasa/bin/activate
cd /home/ubuntu/RASA/WEB-CHAT
rasa run -m enable-api --cors "*" -p 5056
deactivate
