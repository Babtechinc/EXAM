   $( document ).ready(function() {
                $( "#btn" ).click(function() {
                    $( "#box1 option:selected" ).each(function() {
                        $(this).remove().appendTo("#box2")
    });

});
 $( "#btn1" ).click(function() {
                    $( "#box2 option:selected" ).each(function() {
                        $(this).remove().appendTo("#box1")
    });
});
});
