# Know The States

"Know The States" is a Streamlit application that leverages Generative AI (GenAI) to provide users with information about the states of a selected country. The application uses the Groq language model to fetch the states of the selected country.

## How It Works

1. **User Interaction**: Users interact with the application through a web interface built with Streamlit. They can select a country from the sidebar.
2. **GenAI Integration**: Upon selecting a country, the application generates a prompt and sends it to the Groq language model.
3. **Response Handling**: The Groq language model processes the prompt and returns the list of states for the selected country.
4. **Display Results**: The application displays the states of the selected country on the web interface.

## Features

- Select a country from the sidebar.
- View the states of the selected country.
- Utilizes Generative AI to fetch and display information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Know_The_States.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Know_The_States
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to the provided local URL (usually `http://localhost:8501`).

3. Select a country from the sidebar to view its states.

## Dependencies

- Streamlit
- Groq language model


