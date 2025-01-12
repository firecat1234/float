# Contains logic to interact with the language model
# Can be a class to provide context to its methods.
# Add a default model, set by config, and change on the fly.
class LLMService:
    def __init__(self, model_type='mistral'):
         self.model_type = model_type # default model

    def generate_text(self, prompt: str, model_type=None):
        # placeholder for logic that sends a prompt and returns a generation.
        # for now, model_type can be passed to change at runtime.
        # replace with LMStudio call and or API call.
        model = model_type if model_type else self.model_type
        print(f"Generating response using model: {model}")
        return f"Response from {model} for prompt: {prompt}"