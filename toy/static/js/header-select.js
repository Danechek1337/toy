const selectAllElements = document.querySelectorAll("[data-select]");

selectAllElements.forEach(function(item){
    item.addEventListener("click", function(){
        const realSelect = this.nextElementSibling;

        // Если кликнули по пунктам в дропдауне
        if (event.target.hasAttribute("data-select-item") ) {

            // Нашли заголовок у данного дропдауна и записали в его текстовое наполнение значение из data атрибута data-select-item
            var itemTitle = event.target.getAttribute("data-select-item")
            this.querySelector("[data-select-title]").textContent = itemTitle;

            // Скрываем дропдаун
            this.querySelector(".header-select__dropdown").classList.toggle("hidden");

            // Связка с реальным селектом
            // Изменяем значение value у релаьного селекта
            if (realSelect) {
                realSelect.value = itemTitle;
            }

        } else {
            // Если кликнули по заголовку
            // Скрываем или открываем дропдаун
            this.querySelector(".header-select__dropdown").classList.toggle("hidden");
        }


    })
})
