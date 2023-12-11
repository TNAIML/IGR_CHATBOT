To Setup and run this code in local 
* Clone this branch using
`git clone -b new_features_back_contents https://github.com/TNAIML/IGR_CHATBOT.git`

* Make sure you have installed python 3.9 version if you have python 3.9.9+ then rasa framework can't be installed.

* Go to the IGR_CHATBOT Folder create a python environment using 
`python -m venv env`

* Activate the env
-- For windows `.\env\Scripts\Activate`
-- For Ubuntu `Source env/bin/activate` [Confirm  in Offical documentation]

* Once you activated the env install the Rasa using this command
`pip install rasa`

* To run the Project we need 2 terminals(cmd prompt) Navigate to the <b>Test-4</b> Folder and run this command 
`rasa run actions`

* Now another terminal and Navigate to the <b>Test-4</b> Folder and run this command 
`rasa shell`

* In rasa shell you can interact(give input) with the bot in terminal.

* If you made any changes in the code or the data and if you want to reflect those changes in the chat make sure to train the data 

* To train use this command 
`rasa train`

* It uses RNN and LSTM models and it will take around 100epochs