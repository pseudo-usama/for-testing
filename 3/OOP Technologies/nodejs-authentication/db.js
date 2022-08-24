const User = require('./models/user')

function getUser(username) {
  return new Promise(async (res, rej) => {
    try {
      let user = await User.findOne({ username: username })
      res(user)
    }
    catch (err) {
      console.error(err)
      rej()
    }
  })
}

function usernameAlreadyExists(username) {
  return new Promise(async (res, rej) => {
    try {
      let user = await User.findOne({ username: username })
      if (user)
        return res(true)
      res(false)
    }
    catch (err) {
      console.error(err)
      rej()
    }
  })
}

function newUser(username, password, role) {
  return new Promise(async (res, rej) => {
    try {
      const user = new User({
        username: username,
        password: password,
        role: role
      })
  
      const newUser = await user.save()
      res(newUser)
    }
    catch (err) {
      console.error(err);
      rej()
    }
  })
}

module.exports = {
  getUser,
  usernameAlreadyExists,
  newUser,
}
