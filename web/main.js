// csv
let proxies = document.getElementById('proxies');
let credentials = document.getElementById('credentials');
let models = document.getElementById('models');

// send
let run = document.getElementById('run');

const btns = [proxies, credentials, models];
const response = (resp, id) => {
    console.log(resp);
    let element = document.getElementById(id);
    alert.innerHTML = resp['msg'];
    if (resp['type'] === 'error') {
        element.classList.add("text-danger");
    } else {
        element.classList.add("text-success");
    }
}

btns.forEach(async(el) => {
    el.addEventListener('click', async() => {
        await eel.read_csv();
    });
});


run.addEventListener('click', () => {
    // variables+
    let proxies = 0;
    let amountproxie = document.getElementsByClassName('form-check-input');
    if (amountproxie[0].checked) {
        proxies = 1;
    } else {
        proxies = 4;
    }
    let timeawait = document.getElementById('timeawait').value;

    eel.run(timeawait, proxies)(r => console.log(r));

});