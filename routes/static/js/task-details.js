import { showAlert } from './main.js'

const isCompleteDOM = document.querySelector('#completed')
const taskNameDOM = document.querySelector('.task-container > h2')
const taskIdDOM = document.querySelector('#task_id')

isCompleteDOM.onchange = async () => {
  try {
    const resp = await fetch(
      `/dashboard/task/${taskIdDOM.value}/update_completed`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          is_completed: isCompleteDOM.checked,
          task_id: taskIdDOM.value,
        }),
      }
    )
    const data = await resp.json()
    showAlert(data.message, 'alert-success')
    // console.log(data)
    window.location.reload()
  } catch (error) {
    console.log(error)
  }
}
