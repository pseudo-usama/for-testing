require('dotenv').config()

const express = require('express')
const bodyParser = require('body-parser')
const cookieParser = require("cookie-parser");
const jwt = require('jsonwebtoken')
const mongoose = require('mongoose')

const { getUser, usernameAlreadyExists, newUser } = require('./db')

const app = express()
app.use(express.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(cookieParser());


// Routes
app.get('/', signedIn, (req, res) => {
  res.render('index.ejs', { username: req.user.username, role: req.user.role })
})
app.get('/login', notSignedIn, (req, res) => {
  res.sendFile(__dirname + '/public/login.html')
})
app.get('/signup', notSignedIn, (req, res) => {
  res.sendFile(__dirname + '/public/signup.html')
})

app.post('/login', (req, res) => {
  const { username, password } = req.body
  getUser(username)
    .then(user => {
      if (!user || user.password !== password)
        res.status(401).send('Invalid username or password')

      const accessToken = getAccessToken(JSON.stringify(user))
      res.cookie('token', accessToken, { httpOnly: true })
        .redirect('/')
    })
    .catch(() => res.status(500).send())
})

app.post('/signup', async (req, res) => {
  const { username, password, role } = req.body
  if (await usernameAlreadyExists(username))
    return res.status(400).send('Sorry! Username already exists. Try some other')

  newUser(username, password, role)
    .then(user => {
      const accessToken = getAccessToken(JSON.stringify(user))
      res.cookie('token', accessToken, { httpOnly: true })
        .redirect('/')
    })
    .catch(() => res.status(500).send())
})

app.post('/logout', signedIn, (req, res) => {
  res.cookie('token', '', { httpOnly: true })
    .redirect('/signup')
})

// Other functions
function signedIn(req, res, next) {
  const { token } = req.cookies
  if (!token)
    return res.redirect('/signup')

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) {
      console.log(err)
      res.send('authentication error')
    }
    req.user = user
    next()
  })
}

function notSignedIn(req, res, next) {
  const { token } = req.cookies
  console.log(token)
  if (!token)
    return next()

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) {
      console.log(err)
      next()
    }
    res.redirect('/')
  })
}

function getAccessToken(user) {
  return jwt.sign(user, process.env.ACCESS_TOKEN_SECRET)
}

app.listen(4000, () => console.log('Server started'))

// DB connection
mongoose.connect(process.env.DATABASE_URL)
  .then(() => console.log('Database Connected'))
  .catch(err => console.log(err));
