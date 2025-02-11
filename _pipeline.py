import requests
import json
import os
import time

def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    # Find CONFIG
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Load CONFIG
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


def create_payload(model, prompt, target="ollama", **kwargs):
    """
    @NOTE: 
    Need to adjust here to support multiple target formats
    target can be only ('ollama' or 'open-webui')
    """
    payload = None
    if target == "ollama":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}

    elif target == "open-webui":
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }

        # Including other params as options if needed
        payload.update({key: value for key, value in kwargs.items()})
    
    else:
        print(f'!!ERROR!! Unknown target: {target}')
    return payload


def model_req(payload=None):
    """
    COMPLETE
    """
        
    # CUT-SHORT Condition
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    # Send out request to Model Provider
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    # Checking the response and extracting the 'response' field
    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:

        ## @NOTE: Need to adjust here to support multiple response formats
        result = ""
        delta = round(delta, 3)

        response_json = response.json()
        if 'response' in response_json: ## ollama
            result = response_json['response']
        elif 'choices' in response_json: ## open-webui
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return delta, result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    return


###
### DEBUG
###

"""if __name__ == "__main__":
    MESSAGE = "1 + 1"
    PROMPT = MESSAGE 
    payload = create_payload(
                         target="open-webui",  ## instead of "ollama"   
                         model="llama3:latest",  ## instead of "llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

    if payload:
        time_taken, response = model_req(payload=payload)
        print(response)
        if time_taken > 0:
            print(f'Time taken: {time_taken}s')"""
if __name__ == "__main__":
    # Short Message
    MESSAGE_SHORT = "1 + 1"
    PROMPT_SHORT = MESSAGE_SHORT
    payload_short = create_payload(
        target="open-webui",
        model="llama3:latest",
        prompt=PROMPT_SHORT,
        temperature=1.0,
        num_ctx=100,
        num_predict=100
    )

    if payload_short:
        time_taken_short, response_short = model_req(payload=payload_short)
        print("Short Message Response:", response_short)
        if time_taken_short > 0:
            print(f'Short Message Time taken: {time_taken_short}s')

    # Long Message
    MESSAGE_LONG = """Explain the concept of quantum entanglement in simple terms, 
    including its implications for quantum computing and communication.  
    Also, discuss any current research or experiments related to entanglement 
    and its potential future applications."""  # A more complex request
    PROMPT_LONG = MESSAGE_LONG
    payload_long = create_payload(
        target="open-webui",
        model="llama3:latest",
        prompt=PROMPT_LONG,
        temperature=1.0,  # Or a lower temperature for more focused answers
        num_ctx=2048,  # Increase context window if your model supports it
        num_predict=500  # Increase prediction length, as the response will be longer
    )

    if payload_long:
        time_taken_long, response_long = model_req(payload=payload_long)
        print("\nLong Message Response:", response_long)  # Added a newline for clarity
        if time_taken_long > 0:
            print(f'Long Message Time taken: {time_taken_long}s')
