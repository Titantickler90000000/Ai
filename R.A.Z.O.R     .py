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
<!DOCTYPE html>
<html>
<head>
  <title>Popup Example</title>
  <style>
    /* Overlay covering the entire page */
    #popupOverlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      display: none; /* Hidden by default */
      justify-content: center;
      align-items: center;
      z-index: 9999;
    }

    /* Popup box styling */
    #popupBox {
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      width: 300px;
      max-width: 80%;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    /* Close button styling */
    #closePopup {
      margin-top: 10px;
      padding: 8px 16px;
      background-color: #333;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    #closePopup:hover {
      background-color: #555;
    }
  </style>
</head>
<body>

<!-- Popup overlay -->
<div id="popupOverlay">
  <div id="popupBox">
    <h2>Welcome!</h2>
    <p>This is a popup message.</p>
    <button id="closePopup">Close</button>
  </div>
</div>

<!-- Optional button to trigger popup -->
<button onclick="showPopup()">Show Popup</button>

<script>
  // Function to display the popup
  function showPopup() {
    document.getElementById('popupOverlay').style.display = 'flex';
  }

  // Function to hide the popup
  document.getElementById('closePopup').addEventListener('click', function() {
    document.getElementById('popupOverlay').style.display = 'none';
  });

  // Show the popup when the page loads (optional)
  window.onload = function() {
    showPopup();
  };
</script>

</body>
</html>
if __name__ == "__main__":
    ai = RAZOR()
    ai.start()
