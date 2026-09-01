import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Generator", page_icon="🤖")

st.title("🤖 AI Text Generator")
st.write("Enter a topic or prompt and generate AI-powered text.")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct"
    )

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Write a short paragraph about artificial intelligence..."
)

max_tokens = st.slider("Maximum new words/tokens", 50, 300, 150)

if st.button("✨ Generate Text"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating text..."):
            generator = load_model()
            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )
            generated_text = result[0]["generated_text"]

        st.subheader("Generated Text")
        st.write(generated_text)
