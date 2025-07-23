# 🧠 GyaanSagar – Question Answering System using Transformers

## 📌 What is GyaanSagar?

**GyaanSagar** is an interactive Question Answering (QA) tool built using Hugging Face Transformers. It leverages a pre-trained DistilBERT model to answer user-asked questions based on the **SQuAD v1.1** dataset — a large collection of paragraphs and associated questions.

Users can type any question, and the model will intelligently find the most relevant paragraph and extract an answer from it.

---

## ❓ Why this Project?

- 🤖 To explore real-world usage of **Transformer-based models** in NLP.
- 🔍 To simulate a mini **retrieval + extractive QA system** using basic heuristics.
- 💡 To get hands-on with **Hugging Face pipelines**, **SQuAD dataset**, and **BERT family models**.
- 🧪 A foundation for future enhancements like:
  - Web deployment
  - Better paragraph retrieval (semantic similarity)
  - Support for other datasets or domains

---

## ⚙️ How it Works (Under the Hood)

1. **Dataset Parsing**  
   Loads the `dev-v1.1.json` file (SQuAD v1.1 format) and extracts all paragraph-contexts.

2. **Model Setup**  
   Loads the pre-trained model `distilbert-base-uncased-distilled-squad` using Hugging Face's `AutoTokenizer` and `AutoModelForQuestionAnswering`.

3. **Interactive Loop**  
   Accepts user questions through terminal input.

4. **Paragraph Scanning**  
   For each paragraph:
   - Checks if the user question resembles any real question in the dataset.
   - If yes, sends it to the QA pipeline to extract the answer.

5. **Best Match Logic**  
   Out of all matching results, selects the answer with the **highest confidence score**.

6. **Answer Displayed**  
   Final answer is shown to the user.

---

## 🧪 Example Usage

```bash
Enter your question (type 'exit' to quit): What is the capital of France?
Answer: Paris
