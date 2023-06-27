import streamlit as st

# def app():
#     # st.title('Page 2')
#     # st.write('Welcome to page 2')
#     # Contents of page1.py

def app():
    st.title('What are Large Language Models?')
    
    st.header('AI Applications and Large Language Models')
    st.write("AI applications are summarizing articles, writing stories, and engaging in long conversations — and large language models are doing the heavy lifting. A large language model, or LLM, is a deep learning algorithm that can recognize, summarize, translate, predict, and generate text and other forms of content based on knowledge gained from massive datasets.")
    st.write("Large language models are among the most successful applications of transformer models. They aren’t just for teaching AIs human languages, but for understanding proteins, writing software code, and much more.")
    st.write("In addition to accelerating natural language processing applications — like translation, chatbots, and AI assistants — large language models are used in healthcare, software development, and use cases in many other fields.")
    
    st.header('How Do Large Language Models Work?')
    st.write("Large language models learn from huge volumes of data. As its name suggests, central to an LLM is the size of the dataset it’s trained on. But the definition of “large” is growing, along with AI.")
    st.write("Now, large language models are typically trained on datasets large enough to include nearly everything that has been written on the internet over a large span of time.")
    st.write("Such massive amounts of text are fed into the AI algorithm using unsupervised learning — when a model is given a dataset without explicit instructions on what to do with it. Through this method, a large language model learns words, as well as the relationships between and concepts behind them. It could, for example, learn to differentiate the two meanings of the word “bark” based on its context.")
    st.write("And just as a person who masters a language can guess what might come next in a sentence or paragraph — or even come up with new words or concepts themselves — a large language model can apply its knowledge to predict and generate content.")
    st.write("Large language models can also be customized for specific use cases, including through techniques like fine-tuning or prompt-tuning, which is the process of feeding the model small bits of data to focus on, to train it for a specific application.")
    st.write("Thanks to its computational efficiency in processing sequences in parallel, the transformer model architecture is the building block behind the largest and most powerful LLMs.")

    st.header('Top Applications for Large Language Models')
    st.write("Large language models are unlocking new possibilities in areas such as search engines, natural language processing, healthcare, robotics, and code generation.")
    st.write("The popular ChatGPT AI chatbot is one application of a large language model. It can be used for a myriad of natural language processing tasks.")
    st.write("Retailers and other service providers can use large language models to provide improved customer experiences through dynamic chatbots, AI assistants, and more.")
    st.write("Search engines can use large language models to provide more direct, human-like answers.")
    st.write("Life science researchers can train large language models to understand proteins, molecules, DNA, and RNA.")
    st.write("Developers can write software and teach robots physical tasks with large language models.")
    st.write("Marketers can train a large language model to organize customer feedback and requests into clusters, or segment products into categories based on product descriptions.")
    st.write("Financial advisors can summarize earnings calls and create transcripts of important meetings using large language models. And credit-card companies can use LLMs for anomaly detection and fraud analysis to protect consumers.")
    st.write("Legal teams can use large language models to help with legal paraphrasing and scribing.")
    st.write("Running these massive models in production efficiently is resource-intensive and requires expertise, among other challenges, so enterprises turn to NVIDIA Triton Inference Server, software that helps standardize model deployment and deliver fast and scalable AI in production.")
    
    st.caption("Source: [NVIDIA Blog](https://blogs.nvidia.com/blog/2023/01/26/what-are-large-language-models-used-for/)")
