<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Download with Popup</title>
<style>
  #popupOverlay {
    display: none;
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.5);
    justify-content: center; align-items: center;
  }
  #popupBox {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    max-width: 300px;
    text-align: center;
  }
</style>
</head>
<body>

<a href="https://media.tenor.com/7g75zRi40fAAAAAM/dancing-annoying-dog-deltarune.gif" id="downloadLink" download>Download File</a>

<div id="popupOverlay">
  <div id="popupBox">
    <p>Thanks for downloading!</p>
    <button id="closePopup">Close</button>
  </div>
</div>

<script>
  const downloadLink = document.getElementById('downloadLink');
  const popupOverlay = document.getElementById('popupOverlay');
  const closeBtn = document.getElementById('closePopup');

  downloadLink.addEventListener('click', () => {
    popupOverlay.style.display = 'flex';
  });

  closeBtn.addEventListener('click', () => {
    popupOverlay.style.display = 'none';
  });
</script>

</body>
</html>
