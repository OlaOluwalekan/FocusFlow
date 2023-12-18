export const alertDOM = document.querySelectorAll('.alert')
export const FEAlertDOM = document.querySelector('.fe-alert')

// console.log(FEAlertDOM)

alertDOM.forEach((alert) => {
  setTimeout(() => {
    alert.style.display = 'none'
  }, 3000)
})

export const showAlert = (message, type) => {
  FEAlertDOM.textContent = message
  FEAlertDOM.classList.add(type)
  FEAlertDOM.style.display = 'flex'

  setTimeout(() => {
    FEAlertDOM.style.display = 'none'
  }, 3000)
}
