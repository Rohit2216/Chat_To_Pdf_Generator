

# 📝PDF Query Assistant Streamlit App

## Overview

This Streamlit app, named 📝PDF Query Assistant, is designed to assist users in managing PDF documents and querying them efficiently. It provides various features, including PDF uploading, text analysis, and question-answering capabilities.

## Features

- **Home:** A dashboard to navigate through different sections of the app.
- **Account:** User account management.
- **Trending:** Displays trending content related to PDF queries.
- **Query Assistant:** The main feature, allowing users to upload PDFs and ask questions about their contents.
- **About:** Information about the app and its purpose.

## Usage

1. **Configure Firebase API Key:**
   - Before using the app, configure your Firebase API key for user authentication (login, signup, and signout).
   - You can obtain a Firebase API key by following the Firebase documentation.
   - Once you have the API key, create a `.env` file in your project directory and store the key as follows:
     ```
     FIREBASE_API_KEY=your_firebase_api_key_here
     ```
   - This key will be used for user-related functionalities.

2. **Configure OpenAI API Key for PDF Tasks:**
   - To utilize OpenAI's features for PDF analysis, make sure you have obtained an OpenAI API key.
   - Create another entry in your `.env` file to store the OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - This key will be used for PDF-related tasks such as question-answering.

3. Make sure you have Python installed on your system.
4. Install the necessary packages by running `pip install -r requirements.txt`.
5. Run the app using the following command:

   ```bash
   streamlit run main.py


## Contributing

Feel free to contribute to this project by adding new features or fixing issues. Fork the repository, make your changes, and create a pull request. Your contributions are highly appreciated!

## Author

[Rohit Chauhan]

## License

This project is licensed under the [MIT License](LICENSE).

---

Make sure to replace `[Rohit Chauhan]` with your name or the name of the project's primary author. You can also customize this README further to include specific installation instructions or additional details about your app.

Remember to include a `LICENSE` file if you choose a specific open-source license for your project.
