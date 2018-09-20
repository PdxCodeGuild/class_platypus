const addItemInput = document.querySelector('input.addItemInput')
const addItemButton = document.querySelector('button.addItemButton')
const removeItemInput = document.querySelector('input.removeItemInput')
const removeItemButton = document.querySelector('button.removeItemButton')
const strikeItemInput = document.querySelector('input.strikeItemInput')
const strikeItemButton = document.querySelector('button.strikeItemButton')

addItemButton.addEventListener('click', () => {
  let ul = document.getElementsByTagName('ul')[0];
  let li = document.createElement('li');
  li.textContent = addItemInput.value;
  ul.appendChild(li);
  addItemInput.value = '';
})

removeItemButton.addEventListener('click', () => {
  let ul = document.getElementsByTagName('ul')[0];
  let li = document.querySelector('li:last-child');
  ul.removeChild(li);
})