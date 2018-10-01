let addItemInput = document.querySelector('input.addItemInput')
let addItemButton = document.querySelector('button.addItemButton')
let removeItemInput = document.querySelector('input.removeItemInput')
let removeItemButton = document.querySelector('button.removeItemButton')
let strikeItemInput = document.querySelector('.strikeItemInput')
let strikeItemButton = document.querySelector('button.strikeItemButton')
let myOl = document.querySelector('ol')

addItemButton.addEventListener('click', () => {
  let ol = document.getElementsByTagName('ol')[0];
  let li = document.createElement('li');
  li.textContent = addItemInput.value;
  ol.appendChild(li);
  addItemInput.value = '';
})

strikeItemButton.addEventListener('click', () => {
  let active_li = myOl.children[strikeItemInput.value - 1];
  active_li.innerHTML = active_li.innerText;
  active_li.innerHTML = '<del>' + active_li.innerText + '</del>';
  strikeItemInput.value = '';
})

removeItemButton.addEventListener('click', () => {
  let ol = document.getElementsByTagName('ol')[0];
  let li = document.querySelector('li:last-child');
  ol.removeChild(li);
})