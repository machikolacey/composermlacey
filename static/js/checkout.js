 // Update quantity on click
    $('.update-link').click(function(e) {
        const form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        const csrfToken = "{{ csrf_token }}";
        const itemId = $(this).attr('id').split('remove_')[1];
        const size = $(this).data('product_size');
        const url = `/bag/remove/${itemId}/`;
        const data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })