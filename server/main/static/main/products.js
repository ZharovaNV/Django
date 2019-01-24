const renderBook = ({id, image, sauthor, sname}) => (
    `
    <a href="/catalog/${id}/"><img class="imgcatalog" src="${image}" alt="${sauthor}"></a>


    <div class="catalogBook">
        <h4>${sauthor}
            <br>
            ${sname}
        </h4>
        <a href="/catalog/${id}/">Описание</a>
    </div>
    <div class="catalogbuy">
        В наличии 
        <br>
        Доставка на завтра
        <br>
        <input type="button" value="Купить">
    </div>
    <div class="clearfix"></div>
    `
)

