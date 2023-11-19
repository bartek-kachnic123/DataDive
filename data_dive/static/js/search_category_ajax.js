var searchTimeout;
$('#search-input').keyup(function() {
    let query;
    clearTimeout(searchTimeout);

    query = $(this).val();
    if (query.length > 1) {
        $('.fa-hourglass-start').addClass('fa-bounce');
        searchTimeout = setTimeout(function() {
                $.get('/dive/search_category/', {'query': query}, function(data) {
                    const resultList = JSON.parse(data.result_list);
                    $('#result-listing').html(createHtmlContent(resultList));
                    $('.fa-hourglass-start').removeClass('fa-bounce');
                });
            }, 400); // Set a new timeout for 400ms

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
        return htmlParts.join('');
    }


