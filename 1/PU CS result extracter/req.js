const request = require('request')
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0


const URL = 'https://pucit.edu.pk/results/etsresult/mphil/checkResult.php'


function req(rollno) {
    return new Promise((resolve, reject) => {
        request.post(URL, {
            form: {
                rollno: rollno,
                name: ''
            }
        }, (err, res, body) => {
            if (err) {
                console.log(err)
                reject()
                return
            }

            // console.log(body)
            resolve(body)
        })
    })
}


module.exports = { req }
