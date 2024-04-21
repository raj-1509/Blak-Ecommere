let design = {
    text: [],
    stickers: []
  };
  
  function changeTshirt() {
    const tshirtUrl = document.getElementById('tshirt-url').value;
    const tshirtImg = document.getElementById('tshirt');
    tshirtImg.src = "Images\aa-1.png";
  }
  
  function addText() {
    const textInput = document.getElementById('text-input').value;
    const fontSelect = document.getElementById('font-select').value;
    const fontSize = document.getElementById('font-size').value;
  
    const textElement = document.createElement('div');
    textElement.innerText = textInput;
    textElement.style.fontFamily = fontSelect;
    textElement.style.fontSize = fontSize + 'px';
  
    document.getElementById('text-container').appendChild(textElement);
    design.text.push({text: textInput, font: fontSelect, fontSize: fontSize});
  }
  
  function addSticker() {
    const stickerSelect = document.getElementById('sticker-select').value;
  
    const stickerElement = document.createElement('div');
    stickerElement.classList.add('sticker');
    stickerElement.classList.add(stickerSelect);
  
    document.getElementById('sticker-container').appendChild(stickerElement);
    design.stickers.push(stickerSelect);
  }
  
  function addToCart() {
    const cartItem = document.createElement('div');
    cartItem.classList.add('cart-item');
  
    const designAreaClone = document.getElementById('design-area').cloneNode(true);
    cartItem.appendChild(designAreaClone);
  
    document.getElementById('cart').appendChild(cartItem);
  
    // Reset design
    design = {
      text: [],
      stickers: []
    };
  }
  
  