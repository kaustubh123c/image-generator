from monsterapi import client
import requests
import webbrowser

# ✅ Your Monster API key
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ijk1MzVhM2I2NGYxOGNjNWE5OTIxNDgyN2RjZGViZTM1IiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDdUMDk6NTU6NTYuMjE1NTEyIn0.OvAj1ZhteaLpf91A_Z9u74_JBctLQgQe5iWAkjtIpgA"

# Initialize MonsterAPI client
monster_client = client(api_key)

# Prompt from user
prompt = input("Prompt: ")

# Model to use
model = 'txt2img'

# Input data for generation
input_data = {
    'prompt': prompt,
    'negative_prompt': 'bad anatomy',
    'samples': 1,
    'steps': 45,
    'aspect_ratio': 'square',  # options: square, landscape, portrait
    'guidance_scale': 7.3,
    'seed': 2023,
}

# Generate image using MonsterAPI
result = monster_client.generate(model, input_data)

# If 'output' is a list, take the first image URL
img_url = result['output'][0] if isinstance(result['output'], list) else result['output']

file_name = "generated_image.jpg"

# ✅ FIX: Make a request to get the image
response = requests.get(img_url)

# Download image
if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print("Image downloaded successfully!")
    webbrowser.open(file_name)  # Opens the downloaded image
else:
    print("Failed to download the image.")
