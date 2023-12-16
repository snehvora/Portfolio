import streamlit as st
import streamlit_shadcn_ui as ui
from PIL import Image

# Add Google Fonts link to the HTML header
google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">'

st.set_page_config(
    page_title="Sneh Vora | Portfolio",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(google_fonts_link, unsafe_allow_html=True)
# Use custom CSS to set the font to Roboto and make it bold
html_code = """
<style>
    h1 {
        font-family: 'Poppins';
        font-weight: 600;
        letter-spacing: -2px;
        font-size: 80px;
        line-height: 0.9em;
    }
    p, h3, h2, li{
        font-family: 'Poppins';
    }
    /* Media query for larger screens, further adjust line height */
    @media screen and (max-width: 1200px) {
    h1 {
        line-height: 0.6;
    }
    @media screen and (max-width: 768px) {
    h1 {
        line-height: 0.8;
        font-size: 45px;
    }
}
</style>
"""

# Render the HTML code to apply the styling
st.markdown(html_code, unsafe_allow_html=True)

intro_image = Image.open("images/intro-bg.png")
st.image(image=intro_image, width=220)   

st.title(":gray[Hey there!] &nbsp;👋 &nbsp;")
st.title(":gray[I'm] Sneh Vora.")

st.markdown("")

# into cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Visualization", content="BI Tools", description="Power BI", key="card1")
with cols[1]:
    ui.metric_card(title="Machine Learning", content="ML Models", description="ANN, CNN, GANs, RNN, KNN, K-means, SVM", key="card2")
with cols[2]:
    ui.metric_card(title="Natural language", content="LLM", description="Hugging Face, OpenAI", key="card3")

st.markdown("")

# get in touch url links
url_mail = 'mailto:sneh.vora126@gmail.com'
url_linkedIn = 'https://www.linkedin.com/in/sneh-vora-b35358192/'
url_GitHub = 'https://github.com/snehvora'
url_X = 'https://twitter.com/snehvora126'

st.write("Welcome to my portfolio! I am a dedicated and versatile software developer with a strong foundation in backend development, complemented by hands-on experience in Machine Learning projects. My journey has been marked by a commitment to excellence, continuous learning, and a passion for crafting efficient and innovative solutions.")

st.divider()
#Social media icons
st.subheader("Get in touch &nbsp; 🤝")
st.markdown("")
col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.markdown(f'''
    <a href={url_mail}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 37px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>Mail</button></a>
    ''',
    unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <a href={url_linkedIn}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 25px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>LinkedIn</button></a>
    ''',
    unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <a href={url_GitHub}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 30px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>GitHub</button></a>
    ''',
    unsafe_allow_html=True)

with col4:
    st.markdown(f'''
    <a href={url_X}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 47px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>X</button></a>
    ''',
    unsafe_allow_html=True)
    
st.divider()
#Experience   
st.header("💼 &nbsp; Experience")

#BVM
st.subheader("**BVM Infotech Pvt. Ltd., Ahmedabad** &nbsp; :gray[Backend Developer Intern]")
st.caption("Jan 2023 - April 2023.")
st.markdown("- During my internship, I undertook a pivotal role in crafting the backend infrastructure, leveraging the versatility and power of the Flask framework. Flask, renowned as a dynamic Python web framework, served as the cornerstone for developing resilient and streamlined server-side solutions.")

with st.expander("Key Responsibilities"):
    st.markdown("1. **Flask Framework Proficiency :** Demonstrated a deep understanding of Flask, harnessing its capabilities to build robust and flexible server-side applications. ")
    st.markdown("2. **Functionalities Implementation :** Designed and implemented various backend functionalities, focusing on data handling, processing, and management. Ensured seamless interaction between the server and databases for efficient data retrieval and storage.")
    st.markdown("3. **API Integration :** Orchestrated the integration of APIs, facilitating communication between different components of the system. Implemented RESTful API endpoints to enable smooth interaction with frontend applications.")
    st.markdown("4. **Collaborative Teamwork :** Engaged in collaborative efforts with cross-functional teams, contributing to a cohesive and synergistic work environment. Participated in regular meetings and discussions to align backend development with overall project goals.")
    st.markdown("5. **Problem Solving and Optimization :** Resolved complex technical challenges related to backend functionalities, demonstrating a proactive problem-solving approach. Conducted performance analysis and implemented optimizations to enhance the efficiency of the backend processes.")

#Indigenous
st.subheader("**Indigenous Technology, Surat** &nbsp; :gray[Python Developer Intern]")
st.caption("May 2022 - July 2022.")
st.markdown("- Achieved state-of-the-art results in six-way classification problem based on fake news leveraging transfer learning method of fine-tuning BERT model. ")
st.markdown("- Evaluation of model was carried out on benchmark dataset LIAR.")

#Divyam Infotech
st.subheader("**Divyam Infotech Pvt. Ltd., Surat** &nbsp; :gray[Backend Developer Intern]")
st.caption("June 2021 - July 2021.")
st.markdown("- Worked on project ‘topofstyle.com’ wherein we were comparing of several products from different online websites and provide the affiliate link of products to customers for better understanding of price of same product on several online plateforms.")
st.markdown("- Researched about how to scrap data automatically and update in database from time to time withoutany need of monitoring.")
st.divider()

#Teachnook, Bengaluru, Karnataka.
st.subheader("**Teachnook, Bengaluru, Karnataka.** &nbsp; :gray[ML Intern]")
st.caption("Jan 2023 to Feb 2023.")
st.markdown("- My internship at Teachnook provided me with invaluable insights into the practical applications of machine learning in an educational context. I honed my skills in supervised learning, gained hands-on experience with model deployment, and contributed to the advancement of innovative solutions for enhancing the teaching and learning experience. ")
st.markdown("- This internship not only enhanced my technical proficiency but also fostered a passion for leveraging machine learning to address real-world challenges in education.")
st.divider()

#Skills
st.header("🛠 &nbsp; Skills")
st.subheader(":gray[Programming]")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Python")
    st.write("HTML")
with col2:
    st.write("SQl")
    st.write("CSS")
with col3:
    st.write("Javascript")
    st.write("C++")

with col4:
    st.write("PHP")

st.subheader(":gray[General]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Statistical Modelling")
    st.write("Data Visualization")
with col2:
    st.write("Deep Learning")
    st.write("Web Scraping")
with col3:
    st.write("NLP")
    st.write("Git")
with col4:
    st.write("Forecasting")

st.subheader(":gray[Libraries and Frameworks]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Numpy")
    st.write("Tensorflow")
    st.write("Pytorch")
with col2:
    st.write("Pandas")
    st.write("Flask")
    st.write("Beautiful Soup")
with col3:
    st.write("Matplotlib")
    st.write("Selenium")
    st.write("Requests")
with col4:
    st.write("Scikit-learn")
    st.write("Scrapy")

st.subheader(":gray[Visualization Tools]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Power BI")

st.subheader(":gray[Databases]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("PostgreSQl")
with col2:
    st.write("BigQuery")
with col3:
    st.write("MySQl")

st.divider()

# Project Section
st.header("🚀 &nbsp; Projects")

# Wordpress Automation with NLP and AI
st.subheader(":gray[WPInsight Automator]")
st.markdown("- 'WPInsight Automator' is an intelligent WordPress bot seamlessly blending Natural Language Processing (NLP) and Artificial Intelligence (AI) to revolutionize content management. This project combines advanced technologies to extract, paraphrase, and automate tasks within the WordPress ecosystem, ensuring a dynamic and constantly updated website.")

with st.expander("Key Features"):
    st.markdown("1. **News Extraction :**")
    st.markdown("- WPInsight Automator scrapes news information from reputable sources like Hindustan Times, NDTV, and more.")
    st.markdown("- Adaptable to changes: Utilizes dynamic scraping techniques to adjust to variations in website structures.")
    st.markdown("2. **Paraphrasing with AI :**")
    st.markdown("- Employs an API hosted on Digital Ocean for sophisticated paraphrasing, ensuring content uniqueness.")
    st.markdown("- Enhances readability and originality, contributing to a more engaging user experience.")
    st.markdown("3. **Automated WordPress Admin Tasks :**")
    st.markdown("- Manages the WordPress admin autonomously, handling various tasks including post creation, deletion, and status changes.")
    st.markdown("- Ensures seamless and efficient content management, reducing manual intervention.")
    st.markdown("4. **Plagiarized Content Updates :**")
    st.markdown("- Regularly updates the website with news and blog posts, guaranteeing information integrity and originality.")
    st.markdown("- Employs anti-plagiarism measures to maintain content authenticity.")
    st.markdown("5. **Comprehensive Post-Management :**")
    st.markdown("- Handles a range of post-management tasks, including deleting, uploading, and changing post statuses.")
    st.markdown("- Provides robust tools for effective content organization and maintenance.")
    st.markdown("6. **File Management and SEO Integration :**")
    st.markdown("- Manages file uploads seamlessly, ensuring multimedia elements complement the textual content.")
    st.markdown("- Implements Basic SEO techniques through integration with the Rank Math SEO plugin, enhancing the website's search engine visibility.)")
    
st.markdown("")
with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[Selenium]**")
        st.write("**:gray[Numpy]**")
    with col2:
        st.write("**:gray[Tkinter]**")
        st.write("**:gray[math]**")
    with col3:
        st.write("**:gray[smtplib]**")
        st.write("**:gray[Transformers]**")
    with col4:
        st.write("**:gray[PyTorch]**")
        st.write("**:gray[MySQL]**")

# Chatbot using Neural Networks
st.subheader(":gray[Chatbot using Neural Networks]")
st.markdown("- A Chatbot utilizing Long Short-Term Memory (LSTM) neural networks represents a sophisticated and efficient conversational agent. LSTMs are a type of recurrent neural network (RNN) specifically designed to address the vanishing gradient problem, making them well-suited for capturing long-term dependencies in sequential data, such as natural language.")


with st.expander("Key Features"):
    st.markdown("1. **Architecture :** The Chatbot employs a neural network architecture based on LSTM cells. LSTMs enable the model to retain and selectively update information over extended sequences, enhancing the understanding of context in conversations.")
    st.markdown("2. **Natural Language Processing :** The Chatbot incorporates advanced Natural Language Processing (NLP) techniques to comprehend and generate human-like responses. Tokenization, word embeddings, and sequence-to-sequence learning contribute to the model's ability to grasp the nuances of language.")
    st.markdown("3. **Training Data :** The Chatbot is trained on vast datasets comprising diverse and contextually rich conversations. The training data includes dialogues, allowing the model to learn patterns, context, and semantic relationships within the language.")
    st.markdown("4. **Contextual Understanding :** Thanks to LSTM's inherent ability to maintain context over longer sequences, the Chatbot excels at understanding and responding coherently to multi-turn conversations. It recognizes the importance of context in delivering relevant and contextually aware replies.")
    st.markdown("5. **User Interaction :** The Chatbot engages users in natural and intuitive conversations. It can handle a variety of inputs, including questions, statements, and requests, adapting its responses based on the ongoing dialogue.")
    st.markdown("6. **Learning and Adaptation :** The Chatbot continuously learns and adapts its responses based on user interactions. It leverages feedback loops to improve its understanding of user preferences, language nuances, and emerging conversational trends.")
    st.markdown("7. **Real-time Responsiveness :** The model is optimized for real-time responsiveness, ensuring quick and efficient communication. This is crucial for creating a seamless and natural conversational experience for users.")
    st.markdown("8. **Integration :** The Chatbot can be seamlessly integrated into various platforms, such as websites, messaging apps, or customer support systems. Its versatility allows it to adapt to different use cases and industries.")


st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[NumPy]**")
    with col2:
        st.write("**:gray[Pandas]**")
    with col3:
        st.write("**:gray[Tensorflow]**")
        

# DeepVision SynthCraft
st.subheader(":gray[DeepVision SynthCraft]")
st.markdown("- 'DeepVision SynthCraft' is an advanced deep learning project leveraging the cutting-edge technology of Deep Convolutional Generative Adversarial Networks (DCGANs). DCGANs have proven to be more powerful than ordinary GANs, and this project harnesses their capabilities for the synthesis of high-quality images.")

with st.expander("Key Features"):
    st.markdown("1. **DCGAN Architecture :** The project employs the sophisticated architecture of DCGANs, which integrates deep convolutional layers for enhanced feature extraction and generation. This architecture enables the model to produce realistic and visually appealing images.")
    st.markdown("2. **Enhanced Image Synthesis :** Unlike traditional GANs, DCGANs excel in capturing intricate patterns and details, leading to the generation of more realistic and high-resolution images. The project focuses on pushing the boundaries of image synthesis, producing results that are visually stunning and exhibit a high level of fidelity.")
    st.markdown("3. **Epoch-Based Image Saving :** Images are a snapshot of the learning process. In 'DeepVision SynthCraft,' output images are saved at regular intervals, specifically every 100 epochs. This provides an insightful visual journey showcasing the evolution of the model's ability to generate increasingly sophisticated and realistic images over the training period.")
    st.markdown("4. **gan_images Folder :** All generated images are systematically organized and stored in the 'gan_images' folder. This structured approach facilitates easy access, analysis, and comparison of images at different stages of the training process.")
    st.markdown("5. **Creative Exploration :** 'DeepVision SynthCraft' encourages creative exploration, allowing users to witness the diversity and creativity inherent in the generated images. The project offers a canvas for artistic expression through the lens of artificial intelligence.")


st.markdown("")
with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[Numpy]**")
    with col2:
        st.write("**:gray[Sklearn]**")
    with col3:
        st.write("**:gray[tensorflow]**")
    with col4:
        st.write("**:gray[Matplotlib]**")

# Education
st.header("📒 &nbsp; Education")

st.markdown("")

data = {
    'Institution' : ['Sarvodaya Sr Sec School Ranpur Kota, Rajasthan.', 'Om Shanti Eng. Med. School Morbi Rajkot, Gujarat.', 'CHARUSAT University'],
    'Level' : ['10th grade', '12th Grade', 'Undergraduate'],
    'Percentage' : ['95', '75', '88 ']
}

st.dataframe(data=data, use_container_width=True)