import math
import json
import os

class RazorMemory:
    def __init__(self, filename="razor_brain.json"):
        self.filename = filename
        self.knowledge = self.load()
        self.current_topic = None

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.knowledge, f, indent=4)
        except Exception:
            pass  # Silently fail if in a restricted environment like CodeHS

class RazorMath:
    def __init__(self):
        pass

    def calculate(self, expr):
        try:
            expr = expr.replace("^", "**").replace("x", "*")
            return eval(expr, {'__builtins__': None, 'sqrt': math.sqrt, 'pi': math.pi, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'pow': pow})
        except:
            return None

class RAZOR:
    def __init__(self):
        self.brain = RazorMemory()
        self.math = RazorMath()

    def learn(self, query):
        print(f"R.A.Z.O.R: I don't know about '{query}' yet.")
        info = input("Explain it to me: ")
        self.brain.knowledge[query.lower()] = info
        self.brain.save()
        return f"Understood. I have linked '{query}' to: {info}"

    def get_response(self, user_in):
        user_in = user_in.lower().strip()
        # 1. Try Math
        math_res = self.math.calculate(user_in)
        if math_res:
            return math_res
        # 2. Topic Tracking
        if "tell me more" in user_in and self.brain.current_topic:
            return f"Regarding {self.brain.current_topic}: {self.brain.knowledge.get(self.brain.current_topic)}"
        # 3. Known Knowledge
        if user_in in self.brain.knowledge:
            self.brain.current_topic = user_in
            return self.brain.knowledge[user_in]
        # 4. Learning Fallback
        return self.learn(user_in)

    def start(self):
        print("--- R.A.Z.O.R. ONLINE ---")
        while True:
            u = input("\nYou: ")
            if u.lower() in ['exit', 'quit']:
                break
            response = self.get_response(u)
            print(f"R.A.Z.O.R: {response}")

def speak(text):
    # Voice output for local Python. (Will skip in CodeHS)
    try:
        from gtts import gTTS
        import platform
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        if platform.system() == "Darwin":
            os.system("afplay speech.mp3")
        elif platform.system() == "Windows":
            os.system("start speech.mp3")
        else:
            os.system("xdg-open speech.mp3")
    except ImportError:
        pass  # gTTS not installed

if __name__ == "__main__":
    ai = RAZOR()
    ai.start()
