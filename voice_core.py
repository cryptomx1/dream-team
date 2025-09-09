import sys
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "openai/gpt-oss-20b"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)

print("VoiceCore ready. Type 'exit' to quit.")

while True:
    input_text = input("You: ")
    if input_text.lower() == "exit":
        break
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=200, do_sample=True, top_p=0.95)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("VoiceCore: " + response)