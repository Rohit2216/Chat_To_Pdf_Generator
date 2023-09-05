import streamlit as st

def app():
    st.markdown(
        """
        <h1 style='display: flex; align-items: center;'>
            <span style='font-size: 48px; color: orange;'>📝PDF </span>
            <span style='font-size: 48px; color: white;'>Query</span>
            <span style='font-size: 48px; color: green;'>Assistant</span>
        </h1>
        """,
        unsafe_allow_html=True
    )


    st.subheader('Trending thoughts')

    st.write("Explore the latest and most thought-provoking ideas from our community.")
    
    # Placeholder for trending thoughts (replace with real-time data)
    trending_thoughts = [
        {
            "id": 1,
            "title": "The Power of Positive Thinking",
            "author": "User123",
            "content": "In a world full of challenges, maintaining a positive mindset can make all the difference...",
            "likes": 256,
            "comments": [],
            "shares": 12,
        },
        {
            "id": 2,
            "title": "Exploring the Universe",
            "author": "Stargazer456",
            "content": "Join me on a journey through the cosmos as we unravel the mysteries of space...",
            "likes": 312,
            "comments": [],
            "shares": 23,
        },
        {
            "id": 3,
            "title": "Thoughts on AI Ethics",
            "author": "TechEthicist",
            "content": "Ethical considerations in AI development are crucial for a better future...",
            "likes": 178,
            "comments": [],
            "shares": 9,
        },
    ]

    # User submission for trending thoughts
    st.subheader('Submit Your Own Trending Thought')
    user_author = st.text_input("Your Name")
    user_thought_title = st.text_input("Thought Title")
    user_thought_content = st.text_area("Your Thought")

    # List to store user-submitted thoughts
    user_submitted_thoughts = []

    if st.button("Submit"):
        if user_author and user_thought_title and user_thought_content:
            # Process and add the user's thought to the user_submitted_thoughts list
            user_thought = {
                "id": len(user_submitted_thoughts) + 1,
                "title": user_thought_title,
                "author": user_author,
                "content": user_thought_content,
                "likes": 0,
                "comments": [],
                "shares": 0,
            }
            user_submitted_thoughts.insert(0, user_thought)
            st.write("Thank you for sharing your thought!")

    # Display all thoughts including user-submitted thoughts
    all_thoughts = user_submitted_thoughts + trending_thoughts
    for thought in all_thoughts:
        st.write(f"### {thought['title']}")
        st.write(f"**Author**: {thought['author']}")
        st.write(f"{thought['content']}")
        
        # Display like count and provide a button to like
        liked = st.button(f"👍 Like ({thought['likes']})", key=f"like_{thought['id']}")
        if liked:
            thought['likes'] += 1
            st.write("You liked this thought!")
        
        # Comment section
        comment = st.text_input(f"💬 Leave a comment on '{thought['title']}'")
        if comment:
            thought['comments'].append(comment)
            st.write("Comment posted: ", comment)
        
        st.write("💬 Comments:")
        for c in thought['comments']:
            st.write(f"- {c}")
        
        st.write(f"🚀 {thought['shares']}")
        st.write("---")

