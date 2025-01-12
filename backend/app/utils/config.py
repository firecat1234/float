import os
import json

def load_config(config_path='./config.json'):
    """
    Load configuration from a JSON file.
    """
    config = {
        "llm_model": "mistral", # can change via prompt, will be useful for model swap
        "database_type": "sqlite",
        "debug_mode": True,
        # add other configurations
    }

    # check if file exists, then merge with default settings.
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                file_config = json.load(f)
                config.update(file_config) # overwrite existing with json
            except Exception as e:
                print(f"Error Loading Config file: {e}")
    else:
        print(f"No config found, using default settings.")
        #write config file
        with open(config_path, 'w') as outfile:
            json.dump(config, outfile, indent=4) # store defaults for later user

    return config