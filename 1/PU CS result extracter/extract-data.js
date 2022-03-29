const cheerio = require('cheerio')
const querystring = require('querystring')


function extractData(HTML) {
    const $ = cheerio.load(HTML)
    const DATA_URL = $('a').attr('href')

    const data = querystring.parse(DATA_URL)

    data['name'] = data['result.php?name']
    delete data['result.php?name']

    data['status'] = data['correct']
    delete data['correct']

    data['rollno'] = data['rolno']
    delete data['rolno']

    return data
}


module.exports = { extractData }
