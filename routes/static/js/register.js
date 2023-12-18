import { showAlert } from './main.js'

const emailInputDOM = document.querySelector('#email')
const usernameInputDOM = document.querySelector('#username')
const passwordInputDOM = document.querySelector('#password')
const confirmInputDOM = document.querySelector('#confirm')
const registerFormDOM = document.querySelector('.register-form')
const showPasswordDOM = document.querySelector('#show_pass')

// console.log(FEAlertDOM)
showPasswordDOM.onchange = () => {
  if (showPasswordDOM.checked) {
    passwordInputDOM.type = 'text'
    confirmInputDOM.type = 'text'
  } else {
    passwordInputDOM.type = 'password'
    confirmInputDOM.type = 'password'
  }
}

registerFormDOM.onsubmit = (e) => {
  if (!emailInputDOM.value) {
    e.preventDefault()
    showAlert('email is required', 'alert-error')
    return
  }
  if (!usernameInputDOM.value) {
    e.preventDefault()
    showAlert('username is required', 'alert-error')
    return
  }
  if (!passwordInputDOM.value) {
    e.preventDefault()
    showAlert('password is required', 'alert-error')
    return
  }
  if (confirmInputDOM.value != passwordInputDOM.value) {
    e.preventDefault()
    showAlert('password must match', 'alert-error')
    return
  }
}
