import { showAlert } from './main.js'

const categoryFormDOM = document.querySelector('.create-category-form')
const categoryDOM = document.querySelector('.create-category-form > select')
const colorSelectDOM = document.querySelector('#color')
const otherInputDOM = document.querySelector('#other')

categoryDOM.onchange = () => {
  if (categoryDOM.value == 'Custom') {
    otherInputDOM.style.display = 'block'
  } else {
    otherInputDOM.style.display = 'none'
  }
}

categoryFormDOM.onsubmit = (e) => {
  // console.log(otherInputDOM.value)
  if (categoryDOM.value == '') {
    e.preventDefault()
    showAlert('Select a Category', 'alert-error')
    return
  }
  if (categoryDOM.value == 'Custom' && !otherInputDOM.value) {
    e.preventDefault()
    showAlert('Select a Category', 'alert-error')
    return
  }
}
