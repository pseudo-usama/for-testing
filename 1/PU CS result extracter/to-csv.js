const fs = require('fs')
const { parse } = require('json2csv')


const FIELDS = ['rollno', 'name', 'fname', 'score', 'ObtainedMarks', 'status']


function toCSV(data, fileName) {
    try {
        const dataForCSV = parse(data, FIELDS)

        fs.writeFile(`${fileName}.csv`, dataForCSV, (err) => {
            if (err) {
                return console.log(err)
            }
            console.log('The file was saved!')
        })
    }
    catch (err) {
        console.log(err)
    }
}


module.exports = { toCSV }
