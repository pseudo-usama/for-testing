const express = require('express')
const request = require('axios')
const clipboardy = require('clipboardy')
const { default: axios } = require('axios')

require('dotenv').config()

const app = express()


const cookies = [
    'acct=t=lc0XlyFw2NEi1HnLIdi5rfCZbdO%2bBAAk&s=ccrn%2fKSGbDRKCd%2b7FiWNy5WoblQ8l9LA',
    '_gid=GA1.2.1403516227.1630123815',
    '_dlt=1',
    '__qca=P0-563205211-1624196655969',
    'OptanonConsent=isIABGlobal=false&datestamp=Tue+Mar+30+2021+18%3A55%3A06+GMT%2B0500+(Pakistan+Standard+Time)&version=6.10.0&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1',
    'prov=5aaf0113-1112-24bd-bd4a-79c5ffdda9b7',
    '_ga=GA1.2.1340648604.1590326013',
    'OptanonAlertBoxClosed=2021-03-30T13:55:06.269Z',
    '__gads=ID=773d791647472787-22aaa67c41a700b3:T=1617084433:S=ALNI_MZULfKw3fwD6vHqE4Wut2DJCEWfcA',
    'notice-ssb=4%3B1621959511346'
].join(';')


axios.request({
    url: 'https://stackoverflow.com/',
    method: 'get',
    headers: {
        Cookie: process.env.cookies
    }
})
    .then(res => {
        clipboardy.write(res.data)
        // console.log(Object.keys(res))
    })
    .catch(err => {
        console.error(err)
    })


// app.listen(5000 || process.env.PORT)
