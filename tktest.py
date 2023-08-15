from tkinter import *
from tkinter import font
from llama_cpp import Llama
from threading import Thread

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # Initialize the chat interface
        self.init_window()

        # Initialize the LLM model
        self.llm = Llama(model_path="C:/Users/hirot/Python/VSC/AoS/Llama2/llama-2-7b-chat.ggmlv3.q8_0.bin")

    # Initialize the window
    def init_window(self):
        self.master.title("LLM Chat")
        self.pack(fill=BOTH, expand=1)

        # Add a text box for the chat
        chat_font = font.Font(size=14)
        self.chat_text = Text(self, font=chat_font)
        self.chat_text.pack(side=TOP, fill=BOTH, expand=True)
        self.chat_text.config(state=DISABLED)
        self.chat_text.tag_configure("user",background="lightblue")
        self.chat_text.tag_configure("llm", background="lightgreen")

        # Add a status label
        self.status_label = Label(self, text="")
        self.status_label.pack(side=TOP, fill=X)

        # Add a text entry box for typing
        self.text_entry = Entry(self, bd=5)
        self.text_entry.pack(side=LEFT, fill=BOTH, expand=True)
        self.text_entry.bind('<Return>', lambda event: self.send_message())
        
        # Add a send button
        button_font = font.Font(size=10,weight="bold")
        self.send_button = Button(self, text="Send", command=self.send_message,bg="lightblue",fg="darkblue",font=button_font,relief="ridge",bd=3)
        self.send_button.pack(side=RIGHT)

    # Add a message to the chat
    def add_message(self, user, message):
        self.chat_text.config(state=NORMAL)
        tag = "user" if user == "User" else "llm"
        self.chat_text.insert(END, "{}: {}\n".format(user, message), tag)
        self.chat_text.config(state=DISABLED)

    # Update the status message
    def update_status(self, status):
        self.status_label.config(text=status)

    # Generate a response using the LLM model
    def generate_response(self):
        # Get the entire chat history
        chat_history = self.chat_text.get("1.0", END)

        # Append Instruction and Response tags to the chat history
        chat_history = chat_history + "\n Response:\n"
        print(chat_history)
        # Update the status
        self.update_status("Generating response...")

        # Generate a response using the LLM model
        response = self.llm(chat_history, max_tokens=500, temperature=0.1, stop=["Instruction:", "Input:", "Response:"], echo=False)

        # Extract the model's response from the returned dictionary
        response_text = response['choices'][0]['text']

        # Remove '### Response:' prefix from response text
        response_text = response_text.replace(' Response:', '').strip()

        # Remove 'role:' part from the response text

        # Add the LLM response to the chat
        self.add_message("LLM", response_text)

        # Clear the text entry box
        self.text_entry.delete(0, 'end')

        # Update the status
        self.update_status("Response generated.")

    # Send a message to the LLM model
    def send_message(self):

        user_message = self.text_entry.get()
        self.add_message("User", user_message)
        self.text_entry.delete(0, 'end')
        Thread(target=self.generate_response).start()


# Create a window
root = Tk()

# Size of the window
root.geometry("800x600")

# Create a chat interface
app = ChatInterface(root)

# Run the program
root.mainloop()
