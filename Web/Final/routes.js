module.exports = function (app) {

    const express = require('express');
    const path = require('path');

    app.use(express.static(__dirname + '/public'));

    app.get('/', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/index.html'));
    });

    app.get('/applyleave', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/ApplyLeave.html'));
    });

    app.get('/approvemc', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/ApproveMc.html'));
    });

    app.get('/clinics', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/Clinics.html'));
    });

    app.get('/contact', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/Contact.html'));
    });

    app.get('/employeeleave', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/employeeLeaveHistory.html'));
    });

    app.get('/importantnotice', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/importantnotice.html'));
    });

    app.get('/leavehistory', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/LeaveHistory.html'));
    });

    app.get('/notification', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/notification.html'));
    });

    app.get('/uploadmc', function (req, res) {
        res.sendFile(path.join(__dirname + '/public/UploadMc.html'));
    });

};