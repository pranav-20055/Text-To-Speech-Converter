import tkinter as tk
from tkinter import filedialog, messagebox
from summarizer import extract_text_from_pdf, summarize_text, speak_text

def summarize_and_speak():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return
    status_label.config(text="Extracting text...")
    root.update()
    try:
        text = extract_text_from_pdf(file_path)
        status_label.config(text="Summarizing...")
        root.update()
        summary = summarize_text(text)
        status_label.config(text="Speaking summary...")
        root.update()
        speak_text(summary)
        status_label.config(text="Done!")
        messagebox.showinfo("Summary", summary[:500] + ("..." if len(summary) > 500 else ""))
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Failed.")

root = tk.Tk()
root.title("📄 PDF Voice Summarizer")
root.geometry("400x200")

title = tk.Label(root, text="📄 PDF Voice Summarizer", font=("Helvetica", 16))
title.pack(pady=10)

btn = tk.Button(root, text="Choose PDF and Summarize", command=summarize_and_speak)
btn.pack(pady=10)

status_label = tk.Label(root, text="Waiting...", fg="blue")
status_label.pack(pady=10)

root.mainloop()
