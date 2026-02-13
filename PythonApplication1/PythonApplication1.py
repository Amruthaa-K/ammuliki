from flask import Flask, render_template_string
import base64
from pathlib import Path

app = Flask(__name__)

image_path = Path.home() / "Downloads" / "photo.jpg"

image_src = ""
if image_path.exists():
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode()
    image_src = f"data:image/jpeg;base64,{image_base64}"
else:
    image_src = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='250' height='250'%3E%3Crect fill='%23ff4b5c' width='250' height='250'/%3E%3Ctext x='50%25' y='50%25' fill='white' font-size='40' text-anchor='middle' dy='.3em'%3E👫%3C/text%3E%3C/svg%3E"

main_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Happy Valentine's Day ❤️</title>
    <style>
        body {{
            font-family: Arial;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            text-align: center;
            color: white;
            padding: 50px;
        }}
        h1 {{ font-size: 50px; }}
        p {{ font-size: 22px; }}
        img {{ width: 250px; border-radius: 15px; margin: 10px; }}
        button {{ background-color: white; color: #ff4b5c; border: none; padding: 15px 30px; font-size: 18px; border-radius: 10px; cursor: pointer; }}
        button:hover {{ background-color: #ff4b5c; color: white; }}
        
        .modal {{ display: none; position: fixed; z-index: 999; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); align-items: center; justify-content: center; }}
        .modal.show {{ display: flex !important; }}
        .modal-content {{ background-color: #ffc0cb; padding: 40px; border-radius: 15px; text-align: center; max-width: 400px; }}
        .modal-content h2 {{ font-size: 36px; margin-bottom: 30px; color: #ff1493; }}
        .button-container {{ display: flex; gap: 20px; justify-content: center; position: relative; }}
        
        .yes-btn {{ background-color: #ff1493; color: white; padding: 15px 40px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; }}
        .yes-btn:hover {{ background-color: #ff69b4; }}
        
        .no-btn {{ background-color: #ff6b9d; color: white; padding: 15px 40px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; position: fixed; transition: all 0.1s ease; }}
        
        .error-msg {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #ff6b9d; color: white; padding: 30px; border-radius: 15px; font-size: 28px; z-index: 2000; animation: bounce 0.5s; text-align: center; }}
        @keyframes bounce {{ 0%, 100% {{ transform: translate(-50%, -50%) scale(1); }} 50% {{ transform: translate(-50%, -50%) scale(1.1); }} }}
    </style>
</head>
<body>
    <h1>Happy Valentine's Day Likiii(Ladduuu) ❤️</h1>
    <p>This page is made specially for you.<br>You are my happiness, my peace, and my forever.</p>
    <img src="{image_src}" alt="Our Photo">
    <br><br>
    <button onclick="openValentine()">Click for Surprise 💌</button>

    <div id="valentineModal" class="modal">
        <div class="modal-content">
            <h2>Will you be my Valentine? 💕</h2>
            <div class="button-container">
                <button class="yes-btn" onclick="sayYes()">Yes! 😍</button>
                <button class="no-btn" id="noBtn">No 😢</button>
            </div>
        </div>
    </div>

    <div id="errorMsg" class="error-msg"></div>

    <script>
        const funnyMessages = [
            "Oops! Button escaped! 😆",
            "Nice try! Keep trying! 🏃",
            "You can't catch me! 🚀",
            "Button.exe has left the chat 👋",
            "Nope nope nope! 😂",
            "I'm too fast for you! ⚡",
            "Did you really think? 😝",
            "Stop trying, say YES! 💕",
            "You'll never catch me! 😜"
        ];
        
        function openValentine() {{
            document.getElementById("valentineModal").classList.add("show");
            setupNoButton();
        }}
        
        function sayYes() {{
            window.location.href = "/love-messages";
        }}
        
        function moveNoButton() {{
            const btn = document.getElementById("noBtn");
            const x = Math.random() * (window.innerWidth - 150);
            const y = Math.random() * (window.innerHeight - 150);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
            
            showFunnyMsg();
        }}
        
        function showFunnyMsg() {{
            const msg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
            const errorDiv = document.getElementById("errorMsg");
            errorDiv.textContent = msg;
            errorDiv.style.display = "block";
            setTimeout(() => {{
                errorDiv.style.display = "none";
            }}, 2500);
        }}
        
        function setupNoButton() {{
            const btn = document.getElementById("noBtn");
            
            btn.addEventListener("mouseover", moveNoButton, false);
            btn.addEventListener("touchstart", (e) => {{ e.preventDefault(); moveNoButton(); }}, false);
            btn.addEventListener("click", (e) => {{ e.preventDefault(); e.stopPropagation(); moveNoButton(); }}, false);
            btn.addEventListener("pointerdown", (e) => {{ e.preventDefault(); moveNoButton(); }}, false);
        }}
    </script>
</body>
</html>
"""

love_messages_page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Love Messages ❤️</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            text-align: center;
            color: white;
            padding: 40px;
            margin: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
        }}
        h1 {{ font-size: 48px; margin-bottom: 30px; }}
        .message-box {{
            background-color: rgba(255, 255, 255, 0.1);
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
            font-size: 26px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            animation: slideIn 0.6s ease;
        }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .kannada-text {{
            font-size: 32px;
            margin: 15px 0;
            font-weight: bold;
        }}
        .english-text {{
            font-size: 18px;
            opacity: 0.9;
            margin-top: 10px;
        }}
        .heart {{ color: #ff1493; }}
        .back-btn {{
            background-color: white;
            color: #ff4b5c;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 30px;
        }}
        .back-btn:hover {{
            background-color: #ff4b5c;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>My Love for You <span class="heart">❤️</span></h1>
        
        <div class="message-box">
            <div class="kannada-text">ನೀನು ನನ್ನ ಜೀವನದ ಅರ್ಥ</div>
            <div class="english-text">You are the meaning of my life</div>
        </div>
        <div class="message-box">
             <div class=I Love You 
        <button class="back-btn" onclick="window.location.href='/'">Back to Home 💕</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(main_page)

@app.route("/love-messages")
def love_messages():
    return render_template_string(love_messages_page)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)