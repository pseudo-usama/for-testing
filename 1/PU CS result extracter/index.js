const req = require('./req').req
const extractData = require('./extract-data').extractData
const toCSV = require('./to-csv').toCSV

const ROLL_NOS = require('./rollnos').ROLL_NOS
const finalData = []


async function start() {
    for (let i = 0; i < ROLL_NOS.length; i++) {
        console.log('Working on', i)
        if (i == 1) break

        let html
        try {
            html = await req(ROLL_NOS[i])
        }
        catch (err) {
            continue
        }

        const data = extractData(html)
        finalData.push(data)
    }

    toCSV(finalData, 'test')
}

start()
