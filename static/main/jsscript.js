
document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('checkbox');
    const body = document.body;

    btn.addEventListener('change', function () {
        if (this.checked) {
            // NIGHT MODE
            body.style.backgroundColor = '#363434';
            body.style.color = '#fff';
            body.style.transition = '0.5s';
        } else {
            // DAY MODE
            body.style.backgroundColor = '#fff';
            body.style.color = '#343333';
            body.style.transition = '0.5s';
        }
    });
});
