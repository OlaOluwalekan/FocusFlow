import { showAlert } from './main.js'

const usernameInputDOM = document.querySelector('#username')
const passwordInputDOM = document.querySelector('#password')
const loginFormDOM = document.querySelector('.login-form')
const showPasswordDOM = document.querySelector('#show_pass')

showPasswordDOM.onchange = () => {
  if (showPasswordDOM.checked) {
    passwordInputDOM.type = 'text'
  } else {
    passwordInputDOM.type = 'password'
  }
}

loginFormDOM.onsubmit = (e) => {
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
}

// showAlert('username is required', 'error')
