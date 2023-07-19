$(document).ready(function() {
    $('#search-form').submit(function(event) {
        event.preventDefault();
        searchDocumentaries();
    });

    $('#search-input').keyup(function() {
        searchDocumentaries();
    });

    function searchDocumentaries() {
        var query = $('#search-input').val();
        $.ajax({
            url: $('#search-form').attr('action'),
            type: 'GET',
            data: {
                'q': query
            },
            success: function(response) {
                $('#documentaries-list').html(response.html);
            },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    }
});
