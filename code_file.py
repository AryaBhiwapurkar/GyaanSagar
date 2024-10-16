from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import json
import time

# Load your JSON file
with open("/content/drive/MyDrive/dev-v1.1.json", "r") as file:
    data = json.load(file)

# Extract relevant paragraphs and questions from the JSON data
relevant_paragraphs = []
for entry in data["data"]:
    for paragraph in entry["paragraphs"]:
        relevant_paragraphs.append(paragraph)

# Initialize the tokenizer and model
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Define the question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# User interactive prompt
while True:
    user_question = input("Enter your question (type 'exit' to quit): ")
    if user_question.lower() == 'exit':
        break

    best_answer = None
    best_score = 0

    # Process each paragraph
    for paragraph in relevant_paragraphs:
        context = paragraph["context"]
        for qa in paragraph["qas"]:
            question = qa["question"]
            if user_question.lower() in question.lower():
                score = qa_pipeline(question=user_question, context=context)["score"]
                if score > best_score:
                    best_score = score
                    best_answer = qa_pipeline(question=user_question, context=context)["answer"]

    print("Answer:", best_answer)
