// alert("js is connected")

$('#add-to-wishlist').on('click', (evt) => {
    evt.preventDefault()
    alert('Handled with jQuery!');
  })

$('#add-to-wishlist').on('click', (evt) => {
    evt.preventDefault();

    const formInputs = {
        'mask_id': $('#mask_id').val(),
    };

    $.post('/make_request_ajax', formInputs, (res) => {
        alert(res);
    });
});

