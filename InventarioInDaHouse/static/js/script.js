$(document).ready(function() {
    console.log('Script inicializado');

    // Usar delegación de eventos para manejar los clicks en los botones
    $(document).on('click', '.toggle-password', function(e) {
        e.preventDefault();
        console.log('Botón de contraseña clickeado');

        const container = $(this).closest('.password-field');
        const hiddenText = container.find('.password-hidden');
        const visibleText = container.find('.password-visible');
        const icon = $(this).find('i');

        if (hiddenText.is(':visible')) {
            hiddenText.hide();
            visibleText.show();
            icon.removeClass('fa-eye').addClass('fa-eye-slash');
        } else {
            hiddenText.show();
            visibleText.hide();
            icon.removeClass('fa-eye-slash').addClass('fa-eye');
        }
    });
});
