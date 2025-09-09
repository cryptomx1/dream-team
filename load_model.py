from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "openai/gpt-oss-20b"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

print("Model loaded successfully.")