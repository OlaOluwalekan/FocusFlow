import { showAlert } from './main.js'

const createTaskFormDOM = document.querySelector('.create-task-form')
const taskNameDOM = document.querySelector('#title')
const taskDescriptionDOM = document.querySelector('#description')

// console.log(taskNameDOM)

createTaskFormDOM.onsubmit = (e) => {
  if (!taskNameDOM.value) {
    e.preventDefault()
    showAlert('Please input a title/name for your task', 'alert-error')
    return
  }
}
