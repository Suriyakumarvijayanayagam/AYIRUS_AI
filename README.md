# Ayirus AI

Ayirus AI is a Streamlit web application that leverages the GenerativeAI API to provide AI-generated content. It can be used for various purposes, including solving Leetcode and Hackerrank problems.

## Getting Started

1. Install the required dependencies:

    ```bash
    pip install streamlit google.generativeai requests beautifulsoup4
    ```

2. Set up your GenerativeAI API key by creating a file named `api.json` with the following structure:

    ```json
    {
        "api": "YOUR_GENERATIVEAI_API_KEY"
    }
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run apptest.py
    ```

## Usage

1. Enter your prompt in the text area on the left sidebar.
2. Click the "Submit" button to generate AI responses.
3. Use the "Leetcode" and "Hackerrank" buttons to tailor the AI responses to specific platforms.

## Features

- **Leetcode Integration:** Quickly generate content related to Leetcode problems.
- **Hackerrank Integration:** Generate content specific to Hackerrank problems.
- **Logging:** Logs user and AI interactions to `logs/chat_log.txt`.
- **Custom Styling:** The app is styled with a unique theme.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Streamlit: [https://streamlit.io/](https://streamlit.io/)
- GenerativeAI: [https://ai.google/discover/generativeai/](https://ai.google/discover/generativeai/)

## Author

Suriyakumar Vijayanayagam- [GitHub Profile](https://github.com/Suriyakumarvijayanayagam)

