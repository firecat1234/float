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

    def generate_text(self, prompt: str, model_type=None):
        model = model_type or self.model_type
        try:
            print(f"Generating text using {model}")
            # Call local model or external API
            response = f"Generated response from {model} for: {prompt}"
            return response
        except Exception as e:
            print(f"Error in text generation: {e}")
            return "Error generating response."
    def preprocess_prompt(self, prompt: str):
        # Insert observational tokens into the prompt
        return f"<obs_start>{prompt}<obs_end>"
