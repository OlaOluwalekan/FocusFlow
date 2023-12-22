const taskContainerDOM = document.querySelectorAll('.task-container')
const deleteOverlayDOM = document.querySelector('.tasks-overlay')
const cancelBtnDOM = document.querySelector('#cancel_btn')

taskContainerDOM.forEach((taskContainer) => {
  const deleteTaskDOM = taskContainer.querySelector('.tasks-delete-task')
  const taskTitle = taskContainer.querySelector('section > a').textContent
  deleteTaskDOM.onclick = () => {
    showDeleteDialog(taskTitle, taskContainer.id)
  }
})

const showDeleteDialog = (text, id) => {
  const textDOM = document.querySelector('.delete-dialog > p > span')
  const inputDOM = document.querySelector('.delete-dialog > input')
  textDOM.textContent = text
  inputDOM.value = id
  deleteOverlayDOM.style.display = 'flex'
}

cancelBtnDOM.onclick = () => {
  deleteOverlayDOM.style.display = 'none'
}
