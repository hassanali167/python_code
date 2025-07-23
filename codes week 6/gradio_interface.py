import gradio as gr

# Define the function to use in the web app
def greet(name):
    return f"Hello, {name}! Welcome to the Gradio app."

# Create the interface
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Launch the web app
demo.launch()
