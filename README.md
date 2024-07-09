# SOAP Note Scribe

SOAP Note Scribe is an application that transcribes audio files, analyzes the transcribed text, and generates SOAP notes. The application uses OpenAI's Whisper for transcription and Anthropic's Claude 3.5 for text analysis.

## Features

- Transcribe audio files to text
- Analyze transcribed text to extract SOAP note components
- Generate and format SOAP notes
- Save SOAP notes to a file
- User-friendly GUI
- Detailed logging
- Graceful error handling

## Setup

### Clone the Repository

1) clone the github repo -> git clone "github.com/awakeningspirit/dentalsoapnote"
2) install the project requirements --> pip3 install -r requirements.txt 
3) create .env file --> enter your OPENAI_API_KEY="api_key" and ANTHROPIC_API_KEY="api_key"
4) create a virtual env --> "python3 -m venv venv"
5) run the app --> "python3 main.py" 

# SOAP Note Scribe

**SOAP Note Scribe** is an innovative application designed to streamline clinical charting by transcribing audio memos into structured SOAP notes. Leveraging advanced AI technologies like OpenAI's Whisper for transcription and Anthropic's Claude 3.5 for text analysis, this tool transforms the way healthcare professionals document patient interactions.

## Features

- **Audio Transcription**: Effortlessly transcribe clinical audio memos or entire appointment recordings into text.
- **Text Analysis**: Extract key information to populate SOAP (Subjective, Objective, Assessment, Plan) note components.
- **Note Generation**: Automatically generate structured SOAP notes ready for review and approval.
- **User-Friendly Interface**: Intuitive GUI for easy interaction and note management.
- **Secure and Compliant**: Ensures data security and compliance with HIPAA standards.

## Setup

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/awakeningspirit/dentistsoapnote.git
    cd dentistsoapnote
    ```

2. **Set Up Environment Variables**:
    Create a `.env` file in the project root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Using the GUI**:
    - **Upload Audio**: Select an audio file for transcription.
    - **Review Draft**: View and edit the generated SOAP note.
    - **Approve Note**: Finalize and save the note with an e-signature.

## Testing

Ensure the functionality of the application with comprehensive tests.

1. **Run Tests**:
    ```bash
    pytest --cov=main tests/
    ```

## Contributing

Contributions are welcome! Please fork this repository, create a new branch for your feature or bug fix, and submit a pull request.

1. **Fork the Repository**:
    Click on the "Fork" button at the top right of this page.

2. **Create a New Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Commit Your Changes**:
    ```bash
    git commit -m "Add some feature"
    ```

4. **Push to the Branch**:
    ```bash
    git push origin feature/your-feature-name
    ```

5. **Open a Pull Request**:
    Submit a pull request to merge your changes into the main branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For more information or support, please contact us at [support@dentistsoapnote.com](mailto:support@dentistsoapnote.com).
