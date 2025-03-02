from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_with_huggingface(text, max_length=1000, min_length=30):
    try:
        # Generate summary
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        raise Exception(f"Failed to summarize text: {str(e)}")