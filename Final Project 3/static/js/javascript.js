$(document).ready(function () {
    $('#submit').click(function (e) {
        e.preventDefault()
        $('#message').html(`
        <div class="alert alert-info alert-dismissible fade show" role="alert">
            Pasien <strong>{{ prediction_text }}</strong> dari penyakit jantung.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`);
    });
});