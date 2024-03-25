from openai import OpenAI
from api_key import key

open_api_key = key
client = OpenAI(api_key=open_api_key)

# response = client.images.generate(
#   model="dall-e-3",
#   prompt="a white siamese cat",
#   size="1024x1024",
#   quality="standard",
#   n=1,
# )

# image_url = response.data[0].url
# print(image_url)