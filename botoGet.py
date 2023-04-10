import boto3
import json
import pickle

from PIL import Image
import numpy as np

# Load your image using PIL
img = Image.open('../../IITD Palmprint V1/Left Hand/011_3.JPG')

# Convert the image to a numpy array
np_array = np.asarray(img)


runtime = boto3.client('sagemaker-runtime')
endpoint_name = 'tensorflow-inference-2023-04-07-16-16-55-986'
content_type = 'application/json'
payload = json.dumps({'instances': [np_array.tolist()]})


response = runtime.invoke_endpoint(EndpointName=endpoint_name,
                                    ContentType=content_type,
                                    Body=payload)

result = json.loads(response['Body'].read().decode())
# return {
#     'statusCode': 200,
#     'body': result
# }

print(result)