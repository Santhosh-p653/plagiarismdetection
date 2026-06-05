import gradio as gr
import spacy

nlp = spacy.load("en_core_web_md")

def check_similarity(text1, text2):
if not text1.strip() or not text2.strip():
return "Please enter both texts."

doc1 = nlp(text1)
doc2 = nlp(text2)

similarity = doc1.similarity(doc2)
percentage = round(similarity * 100, 2)

if percentage >= 80:
    verdict = "Highly Similar"
elif percentage >= 50:
    verdict = "Moderately Similar"
else:
    verdict = "Different"

return f"""

Similarity Score: {percentage}%

Verdict: {verdict}
"""

demo = gr.Interface(
fn=check_similarity,
inputs=[
gr.Textbox(lines=5, label="Document 1"),
gr.Textbox(lines=5, label="Document 2")
],
outputs=gr.Textbox(label="Result"),
title="Text Similarity Checker",
description="Compare two documents using spaCy semantic similarity."
)

if name == "main":
demo.launch(server_name="0.0.0.0")
