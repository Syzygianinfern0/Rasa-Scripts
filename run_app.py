from rasa_core.channels.facebook import FacebookInput
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.agent import Agent


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = FacebookInput(
fb_verify="##############",
# you need tell facebook this token, to confirm your URL
fb_secret="***************************",  # your app secret
fb_access_token="$$$$$$$$$$$$$$$$$$$$$$$4"  # token for the page you subscribed to
)

agent.handle_channels([input_channel], 5004, serve_forever=True)
