$(document).ready(function () {
    var socket = io.connect(location.origin);
    room_number = 0;

    socket.on('connect', function () {
        socket.emit('joined', ' Connected');
    });

    socket.on('message', function (message) {
        console.log(message);
        $('div.list-messages').append('<br>' + $('<div>').text(message.user + ': ' + message.message).html());
    });

    $('div.join_room').click(function () {
        var room = parseInt($(this).parent().parent().attr('id'));
        socket.emit('join_room', {room: room});
        room_number = room;
    });

    $('button.leave_room').click(function () {
        var room = parseInt($(this).parent().parent().parent().attr('id'));
        socket.emit('leave_room', {room: room});
        $('div#'+room).remove();
        room_number = 0;
    });

    $('input#send_msg').click(function () {
        socket.emit('message', {message: $('input[type="text"]').val(), room: room_number});
        $('input[type="text"]').val("");
    });

    $('#message').keypress(function (e) {
        var key = e.which;
        if (key == 13) {
            $('input#send_msg').click();
        }
    })
});