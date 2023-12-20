const fabBtnDOM = document.querySelector('.fab-btn')
const fabMenuDOM = document.querySelector('.fab-menu')
const fabIconDOM1 = document.querySelector('.fab-btn-span1')
const fabIconDOM2 = document.querySelector('.fab-btn-span2')

fabBtnDOM.onclick = () => {
  fabIconDOM1.classList.toggle('hide')
  fabIconDOM2.classList.toggle('show')
  // console.log(fabIconDOM1, fabIconDOM2)
  fabMenuDOM.classList.toggle('show')
}
