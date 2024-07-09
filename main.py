import os
import openai
import requests
import json
import logging
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk

# Load environment variables
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# Setup logging
logging.basicConfig(level=logging.INFO, filename='soapnotescribe.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    try:
        logging.info(f"Starting transcription for {audio_file}")
        audio_data = open(audio_file, "rb").read()
        response = openai.Audio.transcribe("whisper-1", audio_data)
        logging.info("Transcription completed successfully")
        return response['text']
    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        messagebox.showerror("Error", f"Transcription failed: {e}")
        return ""

# Function to analyze text using Anthropic Claude 3.5
def analyze_text(text):
    try:
        logging.info("Starting analysis with Claude 3.5")
        url = "https://api.anthropic.com/v1/claude/completions"
        headers = {
            "Authorization": f"Bearer {anthropic_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": f"Extract the following details for a SOAP note from the provided text:\\n\\n{text}\\n\\nPatient Information, Subjective, Objective, Assessment, Plan",
            "model": "claude-3.5",
            "max_tokens_to_sample": 1024,
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        logging.info("Analysis completed successfully")
        return response.json()['completion']
    except Exception as e:
        logging.error(f"Analysis failed: {e}")
        messagebox.showerror("Error", f"Analysis failed: {e}")
        return ""

# Function to format the SOAP note
def format_soap_note(analysis):
    try:
        logging.info("Formatting SOAP note")
        analysis_dict = json.loads(analysis)
        soap_note = f"""
        **Patient Information:**
        {analysis_dict.get('Patient Information', 'Not provided')}

        **S: Subjective**
        {analysis_dict.get('Subjective', 'Not provided')}

        **O: Objective**
        {analysis_dict.get('Objective', 'Not provided')}

        **A: Assessment**
        {analysis_dict.get('Assessment', 'Not provided')}

        **P: Plan**
        {analysis_dict.get('Plan', 'Not provided')}

        **Signature:**
        - Dr. [Your Name], DDS
        - License No: [Your License No]
        """
        logging.info("SOAP note formatted successfully")
        return soap_note
    except Exception as e:
        logging.error(f"Formatting failed: {e}")
        messagebox.showerror("Error", f"Formatting failed: {e}")
        return ""

# Function to generate SOAP note
def generate_soap_note():
    audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.m4a")])
    if not audio_file:
        return
    transcription_text.delete(1.0, tk.END)
    analysis_text.delete(1.0, tk.END)
    soap_note_text.delete(1.0, tk.END)

    transcription = transcribe_audio(audio_file)
    if transcription:
        transcription_text.insert(tk.END, transcription)
    
        analysis = analyze_text(transcription)
        if analysis:
            analysis_text.insert(tk.END, analysis)
        
            soap_note = format_soap_note(analysis)
            soap_note_text.insert(tk.END, soap_note)

# Function to save SOAP note to file
def save_soap_note():
    soap_note = soap_note_text.get(1.0, tk.END).strip()
    if not soap_note:
        messagebox.showerror("Error", "SOAP note is empty, cannot save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(soap_note)
        messagebox.showinfo("Success", "SOAP note saved successfully.")

# GUI setup
root = tk.Tk()
root.title("SOAP Note Scribe")
root.geometry("900x700")
root.configure(bg='#f0f0f0')

# Style setup
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('TLabel', font=('Arial', 14), padding=10)
style.configure('TFrame', background='#f0f0f0')

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Tabs
frame1 = ttk.Frame(notebook, width=900, height=700)
frame2 = ttk.Frame(notebook, width=900, height=700)
frame3 = ttk.Frame(notebook, width=900, height=700)
notebook.add(frame1, text="Transcription")
notebook.add(frame2, text="Analysis")
notebook.add(frame3, text="SOAP Note")

# Widgets for Transcription tab
transcription_label = ttk.Label(frame1, text="Transcription")
transcription_label.pack(pady=10)
transcription_text = scrolledtext.ScrolledText(frame1, height=20)
transcription_text.pack(pady=10, padx=10)

# Widgets for Analysis tab
analysis_label = ttk.Label(frame2, text="Analysis")
analysis_label.pack(pady=10)
analysis_text = scrolledtext.ScrolledText(frame2, height=20)
analysis_text.pack(pady=10, padx=10)

# Widgets for SOAP Note tab
soap_note_label = ttk.Label(frame3, text="SOAP Note")
soap_note_label.pack(pady=10)
soap_note_text = scrolledtext.ScrolledText(frame3, height=20)
soap_note_text.pack(pady=10, padx=10)

# Generate and Save buttons
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

generate_button = ttk.Button(frame_buttons, text="Generate SOAP Note", command=generate_soap_note)
generate_button.pack(side=tk.LEFT, padx=10)

save_button = ttk.Button(frame_buttons, text="Save SOAP Note", command=save_soap_note)
save_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
