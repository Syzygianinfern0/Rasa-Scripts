# Lazy Rasa Scripts

This is a collection of all scripts or shortcuts I may be using for Rasa training and running automation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Rasa.

NLU
```bash
pip install rasa_nlu
```
CORE
```bash
pip install rasa_core
```
Use Tensorflow for the pipeline.  For intent classification & entity extraction

```bash
pip install rasa_nlu[tensorflow]
```
## Usage

### Training the NLU model
 To train and test the model run:  

``` python nlu_model.py ```

### Training the Rasa Core model

Custom actions to be run on actions.py and deployed on a server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  
 
3. Talk to the chatbot once it's loaded.  

### Starting the interactive training session:

The process of running the interactive session is very similar to training the Rasa Core model:
1. Make sure the custom actions server is running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. The interactive session also creates a graph.html. Be sure to check that out. Start the interactive training session by running:  

``` python train_interactive.py ```  
   
## Deploy on Messenger
### Managing Credentials

Have the following code in credentials.yml for authentication of the deployment of the bot on the Page created

```yaml
  verify: "##########################"
  secret: "**************************"
  page-access-token: "$$$$$$$$$$$$$$$"
```
The endpoint for receiving facebook messenger messages is ```http://localhost:5005/webhooks/facebook/webhook```, replacing the host and port with the appropriate values. This is the URL you should add in the configuration of the webhook.

### The Actual Part
If you’re testing on your local machine (e.g. not a server), you will need to use [ngrok](https://ngrok.com/). This gives your machine a domain name and so that facebook, slack, etc. know where to send messages.

```bash
python -m rasa_core.run -d models/dialogue -u models/nlu/current --port 5002 --credentials credentials.yml
```
   
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

