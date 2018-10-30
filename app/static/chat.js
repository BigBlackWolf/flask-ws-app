$(document).ready(function () {
            var socket = io.connect('http://' + document.domain + ':' + location.port);

            socket.on('connect', function() {
                    socket.emit('joined', 'Connected');
                });

            socket.on('received_message', function(data) {
                    $('div.list-messages').append('<br>' + $('<div>').text(data.user + ': ' + data.message + ' ').html())
                });

            $('input#send_msg').click(function(){
                socket.emit('message', {message: $('input[type="text"]').val()});
                $('input[type="text"]').val("");
            });
        });