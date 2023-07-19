$(document).ready(function() {
    $('#documentary-form').submit(function(event) {
        event.preventDefault();
        var form = $(this)[0];
        var formData = new FormData(form);

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.success) {
                    alert('Documentary registered successfully!');
                    form.reset();
                } else {
                    alert('Failed to register the documentary.');
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    });
});
