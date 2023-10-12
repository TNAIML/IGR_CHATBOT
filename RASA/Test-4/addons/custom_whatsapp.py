from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.channels.channel import UserMessage

class CustomWhatsAppAction(Action):
    def name(self):
        return "action_custom_whatsapp"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        # Check if the incoming message is from your custom WhatsApp connector
        if isinstance(tracker.latest_message, UserMessage) and tracker.latest_message.input_channel == "aisensy":
            # Access the text of the message
            user_text = tracker.latest_message.text

            # Add your custom logic based on the WhatsApp message
            response = self.process_whatsapp_message(user_text)

            # Send the response back to the user
            dispatcher.utter_message(text=response)
        else:
            # Handle messages from other channels or unknown sources
            dispatcher.utter_message(text="Message from an unknown source")
