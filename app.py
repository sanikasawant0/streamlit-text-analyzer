import streamlit as st
from collections import Counter
import re

st.title("📝 Text Analyzer")

text = st.text_area("Enter your text:")

if text:
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)

    word_count = len(words)
    character_count = len(text)
    sentence_count = len([s for s in sentences if s.strip()])

    st.subheader("📊 Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric("Words", word_count)
    col2.metric("Characters", character_count)
    col3.metric("Sentences", sentence_count)

    st.subheader("🔥 Most Common Words")

    common_words = Counter(words).most_common(5)

    for word, count in common_words:
        st.write(f"**{word}** — {count} times")