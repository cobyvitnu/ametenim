     from transformers import T5ForConditionalGeneration, T5Tokenizer

     # Initialize the model architecture and weights
     model = T5ForConditionalGeneration.from_pretrained('t5-small')

     # Initialize the model tokenizer
     tokenizer = T5Tokenizer.from_pretrained('t5-small')

     # Example input
     input_text = "Hello, my dog is cute"
     input_ids = tokenizer.encode(input_text, return_tensors="pt")

     # Generate output
     outputs = model(input_ids=input_ids)
     