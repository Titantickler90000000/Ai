<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>TECHNO Help Popup</title>
<style>
  #technoPopup {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    height: 400px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    display: none;
    flex-direction: column;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    z-index: 9999;
    font-family: Arial, sans-serif;
  }
  #technoHeader {
    background: #333;
    color: #fff;
    padding: 10px;
    cursor: pointer;
    user-select: none;
    text-align: center;
    font-weight: bold;
  }
  #technoBody {
    flex: 1;
    padding: 10px;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
  }
  #response {
    flex: 1;
    margin-bottom: 10px;
    overflow-y: auto;
    font-size: 14px;
  }
  #technoInput {
    width: 100%;
    box-sizing: border-box;
    padding: 8px;
    font-size: 14px;
  }
</style>
</head>
<body>
<div id="technoPopup">
  <div id="technoHeader">TECHNO</div>
  <div id="technoBody">
    <div id="response"></div>
    <input type="text" id="technoInput" placeholder="Type your help request..." />
  </div>
</div>
<script>
  const popup = document.getElementById('technoPopup');
  const header = document.getElementById('technoHeader');
  const responseDiv = document.getElementById('response');
  const input = document.getElementById('technoInput');

  header.onclick = () => {
    popup.style.display = popup.style.display === 'none' || popup.style.display === '' ? 'flex' : 'none';
  };

  input.addEventListener('keydown', async (e) => {
    if (e.key === 'Enter') {
      const userInput = input.value.trim();
      if (userInput === '') return;
      responseDiv.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;
      input.value = '';
      const reply = await getHelpResponse(userInput);
      responseDiv.innerHTML += `<div><strong>TECHNO:</strong> ${reply}</div>`;
      responseDiv.scrollTop = responseDiv.scrollHeight;
    }
  });

  async function getHelpResponse(prompt) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("This is a simulated response. Replace with your API call.");
      }, 500);
    });
  }
</script>
</body>
</html>
