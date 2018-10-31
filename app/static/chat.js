$(document).ready(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function () {
        socket.emit('joined', ' Connected');
    });

    socket.on('message', function (message) {
        $('div.list-messages').append('<br>' + $('<div>').text(message).html());
        console.log(message)
    });

    socket.on('received_message', function (data) {
        var elem = $('div.list-messages');
        elem.append('<br>' + $('<div>').text(data.user + ': ' + data.message + ' ').html());
    });

    $('div.join_room').click(function () {
        socket.emit('join_room', {room: 1});
    });

    $('button.leave_room').click(function () {
        socket.emit('leave_room', {room: 1});
    });

    $('input#send_msg').click(function () {
        socket.emit('message', {message: $('input[type="text"]').val(), room: 1});
        $('input[type="text"]').val("");
    });

    $('#message').keypress(function (e) {
        var key = e.which;
        if (key == 13) {
            $('input#send_msg').click();
        }
    })
});