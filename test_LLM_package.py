from keyword_extractor import KeywordExtractor
from huggingface_hub import login
login()


# Using LLaMA-2 model
llama_extractor = KeywordExtractor(model_name="meta-llama/Llama-2-7b-chat-hf")
keywords = llama_extractor.extract_keywords("Sensitivity calibration of ultrasonic detectors based using ADD diagrams The paper considers basic problems related to utilization of ADD diagrams")
print(keywords)

# Using another model (e.g., Falcon)
# falcon_extractor = KeywordExtractor(model="falcon-model-name")
# keywords = falcon_extractor.extract_keywords("Your input text")
# print(keywords)
