module.exports = function (app) {
  const mysql = require('mysql');
  const path = require('path');
  var formidable = require('formidable'); //library to handle file upload
  const cookieParser = require('cookie-parser'); //for storing data in cookies
  app.use(cookieParser());

  const bodyParser = require('body-parser'); //to parse form
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({
    extended: true
  }));

  //connect db
  const con = mysql.createConnection({
    host: "localhost",
    database: "project",
    user: "root",
    password: "a1b2c3d4e5"
  });
  var pathModule = "/texttools.js";
  var pathLoadMe = "/clinic.txt";
  app.get('/clinic', loadManyBooks);

  con.connect();

  //login and store information in cookie
  app.post('/login', function (req, res) {
    var login = req.body.username;
    var pw = req.body.password;
    //console.log(login);
    var sql = 'SELECT * FROM users WHERE username = ? AND password = ?';
    con.query(sql, [login, pw], function (err, result) {
      if (err) throw err;
      var userdata = JSON.stringify(result);
      //console.log(result);
      if (userdata != "[]") {
        res.cookie("userid", result[0].id);
        //console.log(result[0].type);
        res.cookie("usertype", result[0].type);
        res.cookie("username", result[0].username);
      }
      res.end(userdata);
    });
  });

  //logout and clear cookies
  app.get('/logout', function (req, res) {
    res.clearCookie('userid');
    res.clearCookie('usertype');
    res.clearCookie('username');
    res.redirect('/');
  });

  //set the dashboard of each role type directly
  app.get('/dashboard', function (req, res) {
    var usertype = req.cookies['usertype'];
    if (usertype == "1") {
      res.sendFile(path.join(__dirname + '/public/SupervisorDashboard.html'));
    } else {
      res.sendFile(path.join(__dirname + '/public/EmployeeDashboard.html'));
    }
  });

  //apply urgent leave page
  app.post('/applyleavedb', function (req, res) {
    var email = req.body.email;
    var date = req.body.date;
    var message = req.body.message;
    //get data from cookies
    var userid = req.cookies['userid'];
    console.log(userid);
    var sql = 'INSERT INTO mc (start_date, requester, email, reason) VALUES (?,?,?,?)';
    con.query(sql, [date, userid, email, message], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  //own leave history page
  app.post('/getleavehistory', function (req, res) {
    var userid = req.cookies['userid'];
    var sql = 'SELECT * FROM mc WHERE requester = ?';
    con.query(sql, [userid], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  //employee leave history page
  app.post('/getallemployeehistory', function (req, res) {
    var sql = 'SELECT * FROM users';
    con.query(sql, function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  //write notice page
  app.post('/getsupervisornames', function (req, res) {
    var sql = 'SELECT * FROM users WHERE type="1"';
    con.query(sql, function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  app.post('/sendnotice', function (req, res) {
    var m = req.body.message;
    var s = req.body.supervisor;
    var userid = req.cookies['userid'];
    var username = req.cookies['username'];
    var currentdate = new Date();
    var sql = 'INSERT INTO messages (msg, msg_date, to_super, from_id, from_name) VALUES (?,?,?,?,?)';
    con.query(sql, [m, currentdate, s, userid, username], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  //notifications page
  app.post('/getnotifications', function (req, res) {
    var userid = req.cookies['userid'];
    var sql = 'SELECT * FROM messages WHERE to_super = ? AND acknowledge = 0';
    con.query(sql, [userid], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  app.post('/acknowledge', function (req, res) {
    var msgid = req.body.msgid;
    var sql = 'UPDATE messages SET acknowledge = 1 WHERE id = ?';
    con.query(sql, [msgid], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  //upload mc page 
  app.post('/getdates', function (req, res) {
    var userid = req.cookies['userid'];
    var sql = "SELECT * FROM mc WHERE requester = ? AND approve_status = ''";
    con.query(sql, [userid], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });

  app.post('/uploadmcdb', function (req, res) {
    var form = new formidable.IncomingForm();
    form.keepExtensions = true;
    form.uploadDir = __dirname + '/public/images';
    form.parse(req, function (err, fields, files) {
      if (err) throw err;
      var mcid = fields.startdate; //option value is mc id
      var enddate = fields.enddate;
      var days = fields.number;
      //console.log(files);
      var file = files.myFile.path; //get path of file
      var file = file.replace(/^.*[\\\/]/, ''); //extract filename frm path
      var dir = "/images/" + file;
      //update directory  and days to db
      con.query("UPDATE mc SET end_date = ?, days = ?, mc_img = ?, approve_status = 'Pending' WHERE mc_id = ?", [enddate, days, dir, mcid], function (err) {
        if (err) throw err;
      });
    });
    res.redirect('/uploadmc');
  });

  //leave application page
  app.post('/getleaveapplications', function (req, res) {
    var userid = req.cookies['userid'];
    var sql = "SELECT * FROM mc INNER JOIN users WHERE requester = id AND approve_status = 'Pending'";
    con.query(sql, [userid], function (err, result) {
      if (err) throw err;
      res.end(JSON.stringify(result));
    });
  });


  app.post('/approvedenymc', function (req, res) {
    var mcid = req.body.mcid;
    var stat = req.body.stat;
    var mcdays = req.body.mcdays;
    var approver = req.cookies['username'];
    var sql = "UPDATE mc SET approve_status = ?, approver = ? WHERE mc_id = ?";
    if (stat != "Deny") {
      var updatebalsql = "UPDATE users INNER JOIN mc SET leave_taken = leave_taken + ?  WHERE requester = id AND mc_id = ?";
      con.query(updatebalsql, [mcdays, mcid], function (err1, result1) {
        if (err1) throw err1;
        //console.log(result1);
      });
    }
    con.query(sql, [stat, approver, mcid], function (err, result) {
      if (err) throw err;
      //console.log(result);
      res.end(JSON.stringify(result));
    });
  });
  async function loadManyBooks(req,res) {
    var tools = require(__dirname+pathModule);
    var arr = (tools.fileToArray(__dirname+pathLoadMe));
    var retv = [];
    arr.forEach((line) => {
      var partOf = line.split(",");
      var newBook = {};
      newBook.name = partOf[0];
      newBook.age = partOf[1];
      newBook.opening = partOf[2];
      retv.push(newBook);
    });
    res.send(retv);
  }
};