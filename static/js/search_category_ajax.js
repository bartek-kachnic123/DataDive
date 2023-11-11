$('#search-input').keyup(function() {
    let query;
    query = $(this).val();
    if (query.length > 1) {
        $.get('/dive/search_category/',
        {'query': query},
        function(data) {
            const resultList = JSON.parse(data.result_list);

        $('#result-listing').html(createHtmlContent(resultList));
        })

}});

function createHtmlContent(items) {
        let htmlParts = [];

        items.forEach(function(item) {
            htmlParts.push('<div class="list-group-item">');
            htmlParts.push(`<a href="/dive/category/${item.fields.slug}">`)
            htmlParts.push(`<h3 class="list-group-item-heading">${item.fields.name}</h3>`);
            htmlParts.push('</a>')
            htmlParts.push('</div>');
        });
        console.log(htmlParts.join(''));
        return htmlParts.join('');
    }


