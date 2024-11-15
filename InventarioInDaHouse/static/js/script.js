document.addEventListener('DOMContentLoaded', function () {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach((button) => {
        button.addEventListener('click', function () {
            const container = this.parentElement;
            const passwordText = container.querySelector('.password-text');
            const realPassword = container.querySelector('.real-password');
            const icon = this.querySelector('i');

            if (passwordText.style.display !== 'none') {
                passwordText.style.display = 'none';
                realPassword.style.display = 'inline';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                passwordText.style.display = 'inline';
                realPassword.style.display = 'none';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });
});
