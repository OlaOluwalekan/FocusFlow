const firstNameDOM = document.querySelector('#first_name')
const lastNameDOM = document.querySelector('#last_name')
const submitPersonalDOM = document.querySelector('#submit_personal_btn')
const passwordDOM = document.querySelector('#password')
const confirmDOM = document.querySelector('#confirm')
const submitPasswordDOM = document.querySelector('#change_password_btn')

if (!firstNameDOM.value || !lastNameDOM.value) {
  submitPersonalDOM.disabled = true
  submitPersonalDOM.classList.add('disabled')
}

firstNameDOM.onkeyup = () => {
  if (!firstNameDOM.value || !lastNameDOM.value) {
    submitPersonalDOM.disabled = true
    submitPersonalDOM.classList.add('disabled')
  } else {
    submitPersonalDOM.disabled = false
    submitPersonalDOM.classList.remove('disabled')
  }
}

lastNameDOM.onkeyup = () => {
  if (!firstNameDOM.value || !lastNameDOM.value) {
    submitPersonalDOM.disabled = true
    submitPersonalDOM.classList.add('disabled')
  } else {
    submitPersonalDOM.disabled = false
    submitPersonalDOM.classList.remove('disabled')
  }
}

if (!passwordDOM.value || !confirmDOM.value) {
  submitPasswordDOM.disabled = true
  submitPasswordDOM.classList.add('disabled')
}

passwordDOM.onkeyup = () => {
  if (
    !passwordDOM.value ||
    !passwordDOM.value ||
    passwordDOM.value != confirmDOM.value
  ) {
    submitPasswordDOM.disabled = true
    submitPasswordDOM.classList.add('disabled')
  } else {
    submitPasswordDOM.disabled = false
    submitPasswordDOM.classList.remove('disabled')
  }
}

confirmDOM.onkeyup = () => {
  if (
    !passwordDOM.value ||
    !passwordDOM.value ||
    passwordDOM.value != confirmDOM.value
  ) {
    submitPasswordDOM.disabled = true
    submitPasswordDOM.classList.add('disabled')
  } else {
    submitPasswordDOM.disabled = false
    submitPasswordDOM.classList.remove('disabled')
  }
}

// console.log(passwordDOM, confirmDOM, submitPasswordDOM)
