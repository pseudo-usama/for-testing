fetch('https://api.coinpaprika.com/v1/coins')
    .then(res => console.log(res))
    .catch(err => console.log(err))
