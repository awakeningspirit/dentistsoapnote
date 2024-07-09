import pytest
import main

def test_transcribe_audio(monkeypatch):
    # Mock successful transcription
    def mock_transcribe(model, audio_data):
        return {'text': 'Transcription successful'}
    monkeypatch.setattr(main.openai.Audio, 'transcribe', mock_transcribe)
    
    result = main.transcribe_audio('path/to/mock_audio_file.wav')
    assert result == 'Transcription successful'

def test_transcribe_audio_failure(monkeypatch):
    # Mock failure
    def mock_transcribe(model, audio_data):
        raise Exception("Transcription failed")
    monkeypatch.setattr(main.openai.Audio, 'transcribe', mock_transcribe)
    
    result = main.transcribe_audio('path/to/mock_audio_file.wav')
    assert result == ''

def test_analyze_text(monkeypatch):
    # Mock successful analysis
    def mock_post(url, headers, data):
        class MockResponse:
            def json(self):
                return {'completion': '{"Patient Information": "John Doe", "Subjective": "Pain", "Objective": "Swelling", "Assessment": "Abscess", "Plan": "Antibiotics"}'}
            def raise_for_status(self):
                pass
        return MockResponse()
    monkeypatch.setattr(main.requests, 'post', mock_post)
    
    result = main.analyze_text('Transcription text')
    assert 'John Doe' in result

def test_analyze_text_failure(monkeypatch):
    # Mock failure
    def mock_post(url, headers, data):
        raise Exception("Analysis failed")
    monkeypatch.setattr(main.requests, 'post', mock_post)
    
    result = main.analyze_text('Transcription text')
    assert result == ''

def test_format_soap_note():
    # Mock successful formatting
    analysis = '{"Patient Information": "John Doe", "Subjective": "Pain", "Objective": "Swelling", "Assessment": "Abscess", "Plan": "Antibiotics"}'
    result = main.format_soap_note(analysis)
    assert 'John Doe' in result

def test_format_soap_note_failure():
    # Mock failure
    analysis = 'Invalid JSON'
    result = main.format_soap_note(analysis)
    assert result == ''
