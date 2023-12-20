const categoryColorDOM = document.querySelectorAll(
  '.category-list > div > article'
)

categoryColorDOM.forEach((item) => {
  item.style.backgroundColor = '{{ category["category_color"] }}'
})
