let btn = document.getElementById('run');



btn.addEventListener('click', () => {
    eel.pythonFunction()(r => console.log(r));
    // const proxies = document.getElementById('proxies').files;
    // const credentials = document.getElementById('credentials').files;
    // const models = document.getElementById('models').files;



    // console.log(proxies);
    // eel.add(proxies, models, credentials)(draw)

});
const draw = (data) => {
    document.getElementById('screen').innerHTML = data
}