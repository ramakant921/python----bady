import google.generativeai as genai
import weave


def format_res(text):
    return text.replace('•', '  *')
